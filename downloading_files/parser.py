import argparse

from .config import Config

# estructurar la información de los parámetros
def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-concurrent-jobs", "-m", default=1, type=int)
    parser.add_argument("--part-size", "-s", default=1_000_000, type=int)
    parser.add_argument("--debug-remote-bandwidth", "-r", default=500_000, type=int)
    parser.add_argument("--debug-local-bandwidth", "-b", default=2_500_000, type=int)
    parser.add_argument("--debug-query-base-time", "-q", type=float, default=0.040)
    parser.add_argument("source", type=str)
    parser.add_argument("dest", type=str)
    return parser

# generar la configuración con los parámetros recogidos en la línea de comandos
def get_config() -> Config:
    parser = get_parser()
    args = parser.parse_args()
    return Config(
        source=args.source,
        destination=args.dest,
        part_size=args.part_size,
        max_concurrent_jobs=args.max_concurrent_jobs,
        debug_remote_bandwidth=args.debug_remote_bandwidth,
        debug_local_bandwidth=args.debug_local_bandwidth,
        debug_query_base_time=args.debug_query_base_time
    )
