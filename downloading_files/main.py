import asyncio
import logging

from .config import get_config
from .download_manager import DownloadManager


def main() -> None:
    # configurar el nivel a partir del que se muestra infomación en los logs
    logging.basicConfig(level=logging.INFO)

    # modificar el máximo de tareas simultáneas de la configuración
    config = get_config(part_size=1024*1024, max_concurrent_jobs=10)

    # instanciar el coordinador
    dlmanager = DownloadManager(config)

    # que el coordinador coordine
    asyncio.run(dlmanager.download())


if __name__ == "__main__":
    main()
