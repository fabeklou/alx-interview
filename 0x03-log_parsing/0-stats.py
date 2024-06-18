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
"""

import signal
import sys


def print_metrics():
    """
    Prints the metrics of the log file.
    """
    print("File size: {}".format(total_file_size))
    for code in ordered_status_codes:
        if code in status_codes_freq and status_codes_freq[code] > 0:
            print("{}: {}".format(code, status_codes_freq[code]))


def line_parsing(line):
    """
    Parses a log line and updates the frequency of status codes
    and the total file size.

    Args:
        line (str): The log line to be parsed.
    """
    global total_file_size
    try:
        tokens = line.split()
        if len(tokens) != 9:
            raise
        status_code, file_size = int(tokens[-2]), int(tokens[-1])
        if status_code in status_codes_freq:
            status_codes_freq[status_code] += 1
            total_file_size += file_size
    except Exception:
        pass


line_count = 0
total_file_size = 0
status_codes_freq = {}
ordered_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

for code in ordered_status_codes:
    status_codes_freq[code] = 0


def signal_handler(sig, frame):
    """Handles the interrupt signal to print stats before exiting"""
    print_metrics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            line_parsing(line)
            if line_count % 10 == 0:
                print_metrics()
    except KeyboardInterrupt:
        print_metrics()
