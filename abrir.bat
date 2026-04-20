@echo off
title IKAR Constructora SAS
color 0A
echo.
echo  ==========================================
echo   IKAR Constructora SAS - Servidor Web
echo  ==========================================
echo.

REM Matar proceso previo en puerto 5500
for /f "tokens=5" %%a in ('netstat -aon 2^>nul ^| findstr :5501') do (
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 1 /nobreak >nul

echo  Iniciando servidor...
start /min "" python -m http.server 5501 --directory "C:\Users\camil\Downloads\clo"

timeout /t 2 /nobreak >nul

echo  Abriendo navegador en http://localhost:5501
start "" "http://localhost:5501"

echo.
echo  ✓ Sitio disponible en: http://localhost:5501
echo  (Cierra esta ventana para detener el servidor)
echo.
pause
