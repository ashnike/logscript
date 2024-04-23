import os
import sys
import time
import signal
import re
from collections import Counter
import user_agents
# NGINX log file paths
NGINX_ACCESS_LOG = "/var/log/nginx/access.log"
NGINX_ERROR_LOG = "/var/log/nginx/error.log"

# Function to handle Ctrl+C signal
def signal_handler(sig, frame):
    print("\nMonitoring stopped.")
    main_menu()

# Function to display the main menu
def main_menu():
    while True:
        print("\nChoose an option:")
        print("1. Monitor NGINX access log")
        print("2. Monitor NGINX error log")
        print("3. Analyze NGINX access log")
        print("4. Analyze NGINX error log")
        print("5. Generate summary report for NGINX access log")
        print("6. Generate summary report for NGINX error log")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            monitor_nginx_access_log()
        elif choice == "2":
            monitor_nginx_error_log()
        elif choice == "3":
            analyze_nginx_access_log()
        elif choice == "4":
            analyze_nginx_error_log()
        elif choice == "5":
            generate_access_log_summary()
        elif choice == "6":
            generate_error_log_summary()
        elif choice == "7":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

# Function to monitor NGINX access log
def monitor_nginx_access_log():
    print("Monitoring NGINX access log:", NGINX_ACCESS_LOG)
    try:
        with open(NGINX_ACCESS_LOG, "r") as f:
            # Move the file pointer to the end
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line:
                    print(line.strip())
                time.sleep(0.1)
    except FileNotFoundError:
        print("Error: NGINX access log file not found.")
        main_menu()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

# Function to monitor NGINX error log
def monitor_nginx_error_log():
    print("Monitoring NGINX error log:", NGINX_ERROR_LOG)
    try:
        with open(NGINX_ERROR_LOG, "r") as f:
            # Move the file pointer to the end
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if line:
                    print(line.strip())
                time.sleep(0.1)
    except FileNotFoundError:
        print("Error: NGINX error log file not found.")
        main_menu()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

# Function to analyze NGINX access log
def analyze_nginx_access_log():
    print("Analyzing NGINX access log:", NGINX_ACCESS_LOG)
    try:
        with open(NGINX_ACCESS_LOG, "r") as f:
            lines = f.readlines()
            # Count occurrences of specific patterns
            keyword_counts = Counter()
            for line in lines:
                # Counting occurrences of HTTP status codes
                status_code_match = re.search(r'\s(\d{3})\s', line)
                if status_code_match:
                    status_code = status_code_match.group(1)
                    keyword_counts[status_code] += 1

            # Generate summary report
            if keyword_counts:
                print("HTTP Status Code Counts:")
                for status_code, count in keyword_counts.items():
                    print(f"{status_code}: {count}")
            else:
                print("No relevant data found.")
    except FileNotFoundError:
        print("Error: NGINX access log file not found.")
        main_menu()

# Function to analyze NGINX error log
def analyze_nginx_error_log():
    print("Analyzing NGINX error log:", NGINX_ERROR_LOG)
    try:
        with open(NGINX_ERROR_LOG, "r") as f:
            lines = f.readlines()
            # Count occurrences of specific patterns
            keyword_counts = Counter()
            for line in lines:
                # Counting occurrences of error messages
                error_match = re.search(r'\[error\] (.+?)$', line)
                if error_match:
                    error_message = error_match.group(1)
                    keyword_counts[error_message] += 1

            # Generate summary report
            if keyword_counts:
                print("Top Error Messages:")
                for error_message, count in keyword_counts.most_common(5):
                    print(f"{error_message}: {count}")
            else:
                print("No relevant data found.")
    except FileNotFoundError:
        print("Error: NGINX error log file not found.")
        main_menu()

# Function to generate summary report for NGINX access log
def generate_access_log_summary():
    print("Generating summary report for NGINX access log:", NGINX_ACCESS_LOG)
    try:
        with open(NGINX_ACCESS_LOG, "r") as f:
            lines = f.readlines()
            # Initialize counters for different metrics
            status_code_counts = Counter()
            request_type_counts = Counter()
            browser_counts = Counter()

            for line in lines:
                # Extracting HTTP status codes, request types, and user-agents
                status_code_match = re.search(r'\s(\d{3})\s', line)
                request_type_match = re.search(r'"(GET|POST|PUT|DELETE)', line)
                user_agent_match = re.search(r'"(.+?)"$', line)

                if status_code_match:
                    status_code = status_code_match.group(1)
                    status_code_counts[status_code] += 1

                if request_type_match:
                    request_type = request_type_match.group(1)
                    request_type_counts[request_type] += 1

                if user_agent_match:
                    user_agent_string = user_agent_match.group(1)
                    user_agent = user_agents.parse(user_agent_string)
                    browser = user_agent.browser.family
                    browser_counts[browser] += 1

            # Generate summary report
            print("HTTP Status Code Counts:")
            for status_code, count in status_code_counts.items():
                print(f"{status_code}: {count}")

            print("\nRequest Type Counts:")
            for request_type, count in request_type_counts.items():
                print(f"{request_type}: {count}")

            print("\nBrowser Counts:")
            for browser, count in browser_counts.items():
                print(f"{browser}: {count}")

    except FileNotFoundError:
        print("Error: NGINX access log file not found.")

# Function to generate summary report for NGINX error log
def generate_error_log_summary():
    print("Generating summary report for NGINX error log:", NGINX_ERROR_LOG)
    try:
        with open(NGINX_ERROR_LOG, "r") as f:
            lines = f.readlines()
            # Count occurrences of specific patterns
            error_counts = Counter()
            for line in lines:
                error_match = re.search(r'\[error\] (.+?)$', line)
                if error_match:
                    error_message = error_match.group(1)
                    error_counts[error_message] += 1

            # Generate summary report
            if error_counts:
                print("Top Error Messages:")
                for error_message, count in error_counts.most_common(5):
                    print(f"{error_message}: {count}")
            else:
                print("No relevant data found.")
    except FileNotFoundError:
        print("Error: NGINX error log file not found.")

def main():
    signal.signal(signal.SIGINT, signal_handler)
    main_menu()

if __name__ == "__main__":
    main()
