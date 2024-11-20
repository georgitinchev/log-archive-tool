# Log Archive Tool

A simple command-line tool to compress and archive logs from a specified directory into `tar.gz` files. This tool helps keep systems clean by organizing logs in a separate directory while maintaining the original log data for future reference. The tool logs the date and time of each archive operation, making it ideal for automating log management.

**Note**: This project is inspired by the idea presented on [roadmap.sh](https://roadmap.sh) and aims to help users practice file handling, directory management, and building Unix-based CLI tools.

## Features
- **Directory Compression**: Compresses log files from a specified directory into `tar.gz` files.
- **Log Organization**: Archives logs into a separate directory (`archives/`) to keep the system clean and organized.
- **Logging**: Records the date and time of each archive operation to a log file (`archive_log.txt`) for tracking and reference.
- **CLI Tool**: Runs from the command line, accepting the log directory as an argument.
