import asyncio
import logging
import random

from .config import Config

logger = logging.getLogger("StorageServiceClient")

# FILE_SIZE = 1024 * 512  # 500KB
FILE_SIZE = 30 * 1024 * 1024  # 30MB
OPERATION_BASE_DELAY = 0.040  # milisegundos
REMOTE_BANDWIDTH = 512 * 1024  # 512KB/s
LOCAL_BANDWIDTH = 5 * REMOTE_BANDWIDTH

"""

"""

class Client:

    def __init__(self, config: Config) -> None:
        self.config = config

    # función que genera tiempos de espera aleatorios por factores externos a la aplicación
    # corresponde al tiempo que se tarda en enviar una peticion y recibir una respuesta
    async def random_operation_wait(self) -> None:
        delay = (random.random() + 1) * OPERATION_BASE_DELAY
        await asyncio.sleep(delay)

    # función a la que le pasas la ruta de un archivo y te da el tamaño del mismo
    async def get_file_size(self, source: str) -> int:
        logger.info(f"getting file size for {source}")
        # pausar un rato que corresponde a lo que tarda en responder el servicio
        await self.random_operation_wait()
        return FILE_SIZE

    # self es un parámetro implícito que señala a la instancia de la clase
    # función que devuelve bytes y recibe
    #   - la direccion del archivo a descargar
    #   - el punto de inicio de la descarga. por defecto, apunta al inicio del archivo
    #   - el punto de finalizacion de la descarga. un valor negativo apunta al final
    #     por defecto es -1
    async def download(self, source: str, start: int = 0, end: int = -1) -> bytes:
        await self.random_operation_wait()
        # al apuntar a un valor negativo o mayor que el tamaño del archivo
        # descargar el archivo hasta el final
        if end < 0 or end > FILE_SIZE:
            end = FILE_SIZE
        logger.info(f"downloading file {source} from {start} to {end}")
        # comprobación de que el tamaño del archivo es positivo
        total_size = end - start
        if total_size < 0:
            raise ValueError("attempted to download with negative part size")
        # tiempo simulado de descarga
        # el ancho de banda va a venir limitado por el mas bajo de los siguientes:
        #   - el ancho de banda del origen
        #   - el ancho de banda de nuestra conexion dividido entre el maximo de trabajos
        #     concurrentes
        bandwidth = min(REMOTE_BANDWIDTH, LOCAL_BANDWIDTH / self.config.max_concurrent_jobs)
        #bandwidth = REMOTE_BANDWIDTH
        delay = total_size / bandwidth
        await asyncio.sleep(delay)
        # datos a descargar como una cadena de bytes (falseado con una ristra de w)
        data = b'w' * total_size
        return data
