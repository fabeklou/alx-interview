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

import sys
import signal

total_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the interrupt signal to print stats
    before exiting
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue
        try:
            size = int(parts[-1])
            code = int(parts[-2])
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
        except (ValueError, IndexError):
            continue

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
