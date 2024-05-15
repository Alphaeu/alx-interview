#!/usr/bin/python3

import sys

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None

def print_statistics(lines_count, total_file_size, status_counts):
    print(f'Total file size: {total_file_size}')
    for status_code in sorted(status_counts):
        print(f'{status_code}: {status_counts[status_code]}')
    print()

def main():
    lines_count = 0
    total_file_size = 0
    status_counts = {}

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is None:
                continue

            lines_count += 1
            total_file_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if lines_count % 10 == 0:
                print_statistics(lines_count, total_file_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_statistics(lines_count, total_file_size, status_counts)

if __name__ == "__main__":
    main()

