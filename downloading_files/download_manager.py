import asyncio
import math
import logging

from .config import Config
from .client import Client

logger = logging.getLogger("DLManager")


class DownloadManager:

    # constructor del coordinador
    def __init__(self, config: Config) -> None:
        self.config = config
        self.client = Client(config)
        self._file_size: int = -1
        self.semaphore = asyncio.Semaphore(config.max_concurrent_jobs)

    # obtener el tamaño del archivo del cliente si se desconoce
    async def file_size(self) -> int:
        if self._file_size == -1:
            self._file_size = await self.client.get_file_size(self.config.source)
        return self._file_size

    # obtener el numero de partes a dividir el archivo
    # el número depende del tamaño del archivo y del tamaño de las partes especificado
    # en la configuracion
    async def get_parts_count(self) -> int:
        file_size = await self.file_size()
        # redondear la división hacia arriba
        parts = math.ceil(file_size / self.config.part_size)
        return parts

    # funcion que obtiene los datos de la parte a descargar
    # devuelve una tupla con el indice y los datos
    async def download_part(self, part_index: int) -> tuple[int, bytes]:
        # semaforo que da luz verde para que se ejecuten las tareas
        # cuando hay menos tareas en ejecucion que el límite (max_concurrent_jobs)
        async with self.semaphore:
            source = self.config.source
            start = part_index * self.config.part_size
            end = (part_index + 1) * self.config.part_size
            data = await self.client.download(source, start, end)
        return part_index, data

    # escribir en el archivo una de las partes indicadas
    def write_part(self, part_index: int, data: bytes) -> None:
        with open(self.config.destination, "ab") as f:
            start = part_index * self.config.part_size
            # colocar el puntero
            f.seek(start)
            f.write(data)

    # realizar descargas con una funcion asíncrona
    async def download(self) -> None:
        logger.info(f"Starting download for file {self.config.source}")
        logger.info(f"Downloading to {self.config.destination}")
        # calcular el numero de partes
        parts = await self.get_parts_count()
        logger.info(f"Dividing in {parts} parts")
        # preparar la lista con todas las tareas
        tasks = [self.download_part(i) for i in range(parts)]
        # ir actuando sobre el resultado de cada parte a medida que termina
        for result in asyncio.as_completed(tasks):
            # desempaquetar la tupla
            part_index, data = await result
            logger.info(f"task {part_index} completed!")
            self.write_part(part_index, data)
