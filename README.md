# enviroment

pip + python

visual studio code + docker

# how to install

install with pip in your environment by either
```
pip install .
```

or remotely
```
pip install git+https://github.com/aliciayusvi/downloading_files.git
```

# usage

usage:
```
download_manager source dest [-h] [--max-concurrent-jobs MAX_CONCURRENT_JOBS] [--part-size PART_SIZE] [--debug-remote-bandwidth DEBUG_REMOTE_BANDWIDTH] [--debug-local-bandwidth DEBUG_LOCAL_BANDWIDTH] [--debug-query-base-time DEBUG_QUERY_BASE_TIME] 
```

positional arguments:
```
  source
  dest
```

options:
```
  -h, --help            show this help message and exit
  --max-concurrent-jobs MAX_CONCURRENT_JOBS, -m MAX_CONCURRENT_JOBS
  --part-size PART_SIZE, -s PART_SIZE
  --debug-remote-bandwidth DEBUG_REMOTE_BANDWIDTH, -r DEBUG_REMOTE_BANDWIDTH
  --debug-local-bandwidth DEBUG_LOCAL_BANDWIDTH, -b DEBUG_LOCAL_BANDWIDTH
  --debug-query-base-time DEBUG_QUERY_BASE_TIME, -q DEBUG_QUERY_BASE_TIME
```
# cases
case 1
```
time download_manager fake_source.txt fake_dest.txt -s 30_000_000 -r 5_000_000 -b 15_000_000
time download_manager fake_source.txt fake_dest.txt -m 1 -s 3_000_000 -r 5_000_000 -b 15_000_000

```
case 2
```
time download_manager fake_source.txt fake_dest.txt -s 30_000_000 -r 5_000_000 -b 15_000_000
time download_manager fake_source.txt fake_dest.txt -m 2 -s 15_000_000 -r 5_000_000 -b 15_000_000
time download_manager fake_source.txt fake_dest.txt -m 3 -s 10_000_000 -r 5_000_000 -b 15_000_000
time download_manager fake_source.txt fake_dest.txt -m 4 -s 7_500_000 -r 5_000_000 -b 15_000_000
```
