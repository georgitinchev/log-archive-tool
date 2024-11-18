import os
import tarfile
from datetime import datetime

def compress_logs(log_directory):
    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        print(f"Error: Directory '{log_directory}' does not exist.")
        return

    # Create a timestamped archive name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"

    # Create an archives directory if it doesn't exist
    archive_directory = "./archives"
    os.makedirs(archive_directory, exist_ok=True)

    archive_path = os.path.join(archive_directory, archive_name)

    # Compress the logs into a tar.gz file
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname=os.path.basename(log_directory))
    
    print(f"Logs compressed and saved to: {archive_path}")

def main():
    # Example log directory for initial testing
    log_directory = "/path/to/logs"  # Replace with your log directory
    compress_logs(log_directory)

if __name__ == "__main__":
    main()
