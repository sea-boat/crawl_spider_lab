@echo off
:again
start main.bat
%wait for 10s%
ping -n 120 127.0.0.1>nul
goto again