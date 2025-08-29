#!/bin/bash

# Paths
PROJECT_DIR="/home/ec2-user/devops-projects/project1"
BACKUP_SCRIPT="$PROJECT_DIR/backup.py"
CRON_LOG="$PROJECT_DIR/backups/cron.log"

# Run backup script
if $BACKUP_SCRIPT >> "$PROJECT_DIR/backups/backup.log" 2>&1; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Backup SUCCESS" >> "$CRON_LOG"
else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Backup FAILED" >> "$CRON_LOG"
fi
