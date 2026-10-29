@echo off
rem Double-click this (or the "Start the day" desktop shortcut): shows today's card, then leaves a window open,
rem in this folder, where you type   today done   when you finish the block.
cd /d "%~dp0"
set "PATH=%~dp0;%PATH%"
title Chaos - today
call "%~dp0today.cmd"
echo.
echo   When you've finished the block, type:   today done
echo   Other commands: today more ^| today swap TRACK ^| today week ^| today status
echo.
cmd /k
