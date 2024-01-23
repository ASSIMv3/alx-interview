#!/usr/bin/python3
import sys
from collections import defaultdict
import signal


def print_statistics(total_size, status_counts):
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')


def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    def handle_interrupt(signal, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                ip_address = parts[0]
                date = parts[3][1:]
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if parts[5] == '"GET' and parts[6].startswith('/projects/260') and parts[7] == 'HTTP/1.1"':
                    total_size += file_size
                    status_counts[status_code] += 1
                    lines_processed += 1

                    if lines_processed % 10 == 0:
                        print_statistics(total_size, status_counts)

            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        handle_interrupt(None, None)


if __name__ == "__main__":
    main()
