#!/usr/bin/python3

import re
import signal
import sys


def print_metrics():
    global line_count
    line_count = 0

    print("File size: {}".format(total_file_size))
    for code in ordered_status_codes:
        if code in status_codes_freq and status_codes_freq[code] > 0:
            print("{}: {}".format(code, status_codes_freq[code]))


def signal_handler(signum, frame):
    print_metrics()


line_count = 0
total_file_size = 0
status_codes_freq = {}
ordered_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET \/projects\/260 HTTP\/1.1" \d{3} \d{1,}$'  # noqa

for code in ordered_status_codes:
    status_codes_freq[code] = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        log = line.strip()
        if re.search(pattern, line):
            tokens = log.split(' ')
            method, file_size = int(tokens[-2]), int(tokens[-1])
            if method in status_codes_freq:
                status_codes_freq[method] += 1
                total_file_size += file_size

        if line_count == 10:
            print_metrics()
except Exception as err:
    print(err)
