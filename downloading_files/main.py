import asyncio
import logging

from .download_manager import DownloadManager
from .parser import get_config


def main() -> None:
    # configurar el nivel a partir del que se muestra infomacion en los logs
    logging.basicConfig(level=logging.INFO)

    # modificar el maximo de tareas simultáneas de la configuracion
    config = get_config()

    # instanciar el coordinador
    dlmanager = DownloadManager(config)

    # que el coordinador coordine
    asyncio.run(dlmanager.download())


if __name__ == "__main__":
    main()
