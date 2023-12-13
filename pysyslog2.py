#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse
from datetime import datetime, timedelta
from termcolor import colored

def parse_syslog(log_line, search_string, date=None):
    # Define the regular expression pattern to match the timestamp
    pattern = r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})"

    # Use the regular expression to extract the timestamp
    match = re.search(pattern, log_line)
    if match:
        timestamp_str = match.group(1)

        # Parse the timestamp string into a datetime object
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S")

        # If a date is specified, only return the timestamp if it matches the date
        if date and timestamp.date() != date:
            return None

        # If the search string is in the log line, return the timestamp and log line
        if search_string in log_line:
            colored_log_line = log_line.replace(search_string, colored(search_string, 'red'))
            return timestamp, colored_log_line

    return None

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Parse a syslog file for a specific string and date.',
        epilog='''Examples of usage:
        python3 pysyslog.py -f /path/to/your/file -d 2022-01-01 -s error
        python3 pysyslog.py -f /path/to/your/file -s error
        python3 pysyslog.py -f /path/to/your/file -d $(date -d "2 days ago" +%Y-%m-%d) -s error
        python3 pysyslog.py -f /path/to/your/file -d 2022-01-01 -s error -l 10
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-f", "--file", required=True, help="The file to parse")
    parser.add_argument("-d", "--date", help="The date in question (format: YYYY-MM-DD)")
    parser.add_argument("-s", "--search", required=True, help="The string to search for")
    parser.add_argument("-l", "--limit", type=int, default=float('inf'), help="Limit the number of lines of output")
    args = parser.parse_args()

    # If a date is specified, parse it into a date object
    date = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else None

    # Open the file and parse each line
    limit = args.limit
    with open(args.file, "r") as f:
        for line in f:
            if limit <= 0:
                break
            result = parse_syslog(line, args.search, date)
            if result:
                timestamp, log_line = result
                print("Timestamp:", timestamp)
                print("Log line:", log_line)
                limit -= 1

if __name__ == "__main__":
    main()