from dataclasses import dataclass

DEFAULT_PART_SIZE = 50 * 1024  # KB/s


# clase de configuración
@dataclass
class Config:
    source: str
    destination: str
    part_size: int  # en bytes
    max_concurrent_jobs: int


# función para obtener la configuración desde otras clases con algunos valores por defecto
def get_config(part_size: int = DEFAULT_PART_SIZE, max_concurrent_jobs: int = 1) -> Config:
    # se podrian utilizar parametros de la linea de comandos, pero como de momento
    # esto es solo una 'simulacion', fingimos que obtenemos la configuracion que
    # necesitemos para cada ocasion
    return Config(
        "fake://fakehost:2222/fake/path/filename.txt",
        "./filename.txt",
        part_size,
        max_concurrent_jobs
    )
