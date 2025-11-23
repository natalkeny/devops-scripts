import os
import subprocess
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Define constants
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    WORKDIR = os.path.join(BASE_DIR, 'work')
    LOG_FILE = os.path.join(WORKDIR, 'log.txt')

    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()

    # Get current working directory
    cwd = os.getcwd()

    # Get list of files in the current directory
    files = [f for f in os.listdir(cwd) if os.path.isfile(f)]

    # Iterate over files and run commands
    for file in files:
        if file.endswith('.json'):
            # Get file contents
            with open(os.path.join(cwd, file), 'r') as f:
                data = json.load(f)

            # Run command to process the file
            subprocess.run(['python', '-m', 'json2csv', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Write processed data to log file
            with open(LOG_FILE, 'a') as f:
                f.write(f"{file} -> {json.dumps(data)}\n")

if __name__ == '__main__':
    main()