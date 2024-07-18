#!/bin/bash


# 현재 경로
DIR="/var/log/aiapi"
echo "Current directory: $DIR" >> $DIR/backup_script.log

# 로그 파일 경로
LOG_DIR="$DIR/log"
BACKUP_DIR="$DIR/log/backup"

# 오늘 날짜와 시간
TODAY=$(date +"%Y-%m-%d")
echo "Backup date: $TODAY" >> $DIR/backup_script.log

# 백업 디렉토리 생성
mkdir -p $BACKUP_DIR/$TODAY
echo "Backup directory created: $BACKUP_DIR/$TODAY" >> $DIR/backup_script.log

# 로그 파일 백업
cp $LOG_DIR/*.log $BACKUP_DIR/$TODAY
echo "Log files backed up" >> $DIR/backup_script.log

# 원본 로그 파일 비우기
cat /dev/null > $LOG_DIR/*.log
echo "Original log files cleared" >> $DIR/backup_script.log
