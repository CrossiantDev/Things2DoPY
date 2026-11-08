@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Запуск трекера фокуса...
start "" "index.html"
exit
