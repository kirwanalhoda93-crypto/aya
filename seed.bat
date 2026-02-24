@echo off
chcp 65001 >nul
title AURELIA Database Seeder

echo ============================================
echo    AURELIA Database Seeder
echo ============================================
echo.

cd backend

echo Checking virtual environment...
if not exist "venv" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [IMPORTANT] Make sure:
echo 1. XAMPP MySQL is running
echo 2. Database 'jewelry_db' exists in phpMyAdmin
echo.
pause

echo.
echo Seeding database...
python seeder.py

echo.
pause
