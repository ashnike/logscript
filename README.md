# NGINX Log Analyzer
This Python script provides a comprehensive toolset for monitoring and analyzing NGINX access and error logs. It allows you to:

- Monitor NGINX access and error logs in real-time.
- Analyze log data to extract information such as HTTP status codes, request
types, and browser information.
- Generate summary reports based on log analysis.
## Features
1. **Real-time Log Monitoring**: Monitor NGINX access and error logs continuously, displaying new log entries as they are written.
2. **Log Analysis**: Analyze log data to extract useful information, such as HTTP status codes, request types (GET, POST, etc.), and user-agent strings.
3. **Summary Reports**: Generate summary reports based on log analysis, providing counts of various metrics like HTTP status codes, request types, and browser usage.
### Prerequisites
- Python 3.x
- pip
- NGINX log files accessible to the script (typically located at /var/log/nginx/access.log and /var/log/nginx/error.log).

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/nginx-log-analyzer.git
```
2. Install user_agents python module
```
pip install user_agents
```
2. Navigate to the directory:
```
cd nginx-log-analyzer
```
3. Run the script:
```
python3 nginx_log_analyzer.py
```
Upon running the script, you will be presented with a menu.
Choose an option based on what you want to do (monitor logs, analyze logs, or generate summary reports).
Follow the prompts to interact with the script and view the desired information.
Contributing
Contributions are welcome! Please feel free to fork the repository, make pull requests, and suggest improvements.

