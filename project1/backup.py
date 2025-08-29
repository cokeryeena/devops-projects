#!/usr/bin/env python3
import os
import shutil
import datetime

# Source and destination folders
SOURCE_DIR = "/home/ec2-user/devops-projects/project1"
BACKUP_DIR = "/home/ec2-user/devops-projects/project1/backups"

# Ensure backup folder exists
os.makedirs(BACKUP_DIR, exist_ok=True)

# Log file
log_file = os.path.join(BACKUP_DIR, "backup.log")

with open(log_file, "a") as log:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log.write(f"\n--- Backup started at {timestamp} ---\n")

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".py"):  # only back up Python files
            filepath = os.path.join(SOURCE_DIR, filename)
            dest_path = os.path.join(BACKUP_DIR, filename)
            shutil.copy2(filepath, dest_path)
            log.write(f"Backed up: {filename}\n")

    log.write(f"--- Backup finished at {datetime.datetime.now()} ---\n")

