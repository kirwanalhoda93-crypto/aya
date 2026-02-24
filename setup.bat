@echo off
chcp 65001 >nul
title AURELIA Backend Setup

echo ============================================
echo    AURELIA Jewelry E-commerce Setup
echo ============================================
echo.

echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version
echo.

echo [2/4] Creating virtual environment...
cd backend
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)
echo.

echo [3/4] Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo Dependencies installed successfully.
echo.

echo [4/4] Creating .env file if not exists...
if not exist ".env" (
    copy .env.example .env >nul
    echo .env file created from .env.example
    echo.
    echo [IMPORTANT] Please edit backend\.env and add your GEMINI_API_KEY
    echo.
) else (
    echo .env file already exists.
)
echo.

cd ..

echo ============================================
echo    Setup completed successfully!
echo ============================================
echo.
echo Next steps:
echo 1. Make sure XAMPP MySQL is running
echo 2. Create database 'jewelry_db' in phpMyAdmin
echo 3. Edit backend\.env and add your GEMINI_API_KEY
echo 4. Run start.bat to start the server
echo.
pause
