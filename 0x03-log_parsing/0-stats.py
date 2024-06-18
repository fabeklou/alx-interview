#!/usr/bin/python3

"""
This module is used for parsing log files and generating statistics.

The module reads log entries from the standard input
and calculates the following metrics:
- File size: The total size of the log file.
- Status code frequency: The frequency of each
  HTTP status code in the log file.

The module expects log entries to be in the following format:
<IP Address> - [<Date>] "GET /projects/260 HTTP/1.1" <Status Code> <File Size>

Example:
192.168.0.1 -\
[2022-01-01 12:00:00.000000] "GET /projects/260 HTTP/1.1" 200 1024
"""

import re
import signal
import sys


def print_metrics():
    """
    Prints the metrics of the log file.

    This function prints the file size and the frequency of each status code
    in the log file. It uses the global variables `total_file_size`,
    `ordered_status_codes`, and `status_codes_freq` to retrieve the necessary
    information.

    Parameters:
        None

    Returns:
        None
    """
    global line_count
    line_count = 0

    print("File size: {}".format(total_file_size))
    for code in ordered_status_codes:
        if code in status_codes_freq and status_codes_freq[code] > 0:
            print("{}: {}".format(code, status_codes_freq[code]))


def signal_handler(signum, frame):
    """
    Signal handler function that is called when a signal is received.

    Args:
        signum (int): The signal number.
        frame (frame): The current stack frame at the time
            the signal was received.
    """
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
