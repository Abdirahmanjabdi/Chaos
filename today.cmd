@echo off
rem Start or close the day.  today | today done | today swap TRACK | today more | today week | today status | today doctor
setlocal
where py >nul 2>nul
if %errorlevel% equ 0 (
  py -3 "%~dp0tools\today.py" %*
) else (
  python "%~dp0tools\today.py" %*
)
endlocal
