@echo off
chcp 65001 >nul
title AURELIA Backend Server

echo ============================================
echo    AURELIA Jewelry E-commerce Server
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
echo Checking .env file...
if not exist ".env" (
    echo [ERROR] .env file not found!
    echo Please run setup.bat first.
    pause
    exit /b 1
)

echo.
echo Starting FastAPI server...
echo.
echo Server will be available at:
echo   - API: http://localhost:8000
echo   - Docs: http://localhost:8000/docs
echo   - ReDoc: http://localhost:8000/redoc
echo.
echo Press Ctrl+C to stop the server
echo ============================================
echo.

uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause
