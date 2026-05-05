@echo off
title AI Korjaamo - Starter

echo ================================
echo AI KORJAAMO KAYNNISTYS
echo ================================

echo.
echo Kaynnistetaan Diagnostic Bridge porttiin 8001...
start "Diagnostic Bridge" cmd /k "cd /d %~dp0services\diagnostic-bridge && pip install -r requirements.txt && uvicorn main:app --port 8001"

timeout /t 3 >nul

echo.
echo Kaynnistetaan AI Gateway porttiin 8002...
start "AI Gateway" cmd /k "cd /d %~dp0ai-platform\ai-gateway && pip install -r requirements.txt && uvicorn main:app --port 8002"

echo.
echo Valmis.
echo Avaa selaimessa:
echo http://localhost:8002/docs
echo.
pause
