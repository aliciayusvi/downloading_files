from dataclasses import dataclass

# clase de configuracion
@dataclass
class Config:
    source: str = "fake://fakehost:2222/fake/path/filename.txt"
    destination: str = "./filename.txt"
    part_size: int = 1_000_000  # bytes
    max_concurrent_jobs: int = 1
    debug_remote_bandwidth: int = 500_000  # bytes
    debug_local_bandwidth: int = 2_500_000  # bytes
    debug_query_base_time: float = 0.040  # s
