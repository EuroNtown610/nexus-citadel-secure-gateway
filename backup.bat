@echo off
:: ==========================================
:: SYSTEM DEV WORKSPACE AUTOMATED BACKUP
:: ==========================================

set "SOURCE_DIR=%USERPROFILE%\Desktop\sd-workspace"
set "BACKUP_DIR=E:\sd-workspace-backup"

echo Starting backup of workspace...
echo Source: %SOURCE_DIR%
echo Target: %BACKUP_DIR%
echo ------------------------------------------

:: Run robocopy to mirror the directory structure
:: /MIR  - Mirrors a directory tree (deletes targets if deleted in source)
:: /R:3  - Retry 3 times on failed files
:: /W:5  - Wait 5 seconds between retries
:: /MT:8 - Use multi-threading (8 threads) for faster copy speeds

robocopy "%SOURCE_DIR%" "%BACKUP_DIR%" /MIR /R:3 /W:5 /MT:8

echo ------------------------------------------
echo Backup operation completed successfully!
pause
