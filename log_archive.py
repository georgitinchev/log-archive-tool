import os
import tarfile
from datetime import datetime

def compress_logs(log_directory):
    # Ensure the irectory exists
    if not os.path.exists(log_directory):
        print(f"Error: Directory '{log_directory}' does not exist.")
        return

    # Check if the directory is empty
    if not os.listdir(log_directory):
        print(f"Warning: Directory '{log_directory}' is empty. No logs to compress.")
        return

    # Create a timestamped archive name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"

    # Create archives directory
    archive_directory = "./archives"
    os.makedirs(archive_directory, exist_ok=True)

    archive_path = os.path.join(archive_directory, archive_name)

    # Compress the logs
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname=os.path.basename(log_directory))

    # Log archive details
    with open("archive.log", "a") as log_file:
        log_file.write(f"{timestamp}: {archive_path}\n")

    print(f"Logs compressed and saved to: {archive_path}")

def main():
    log_directory = "/path/to/logs" 
    compress_logs(log_directory)

if __name__ == "__main__":
    main()


