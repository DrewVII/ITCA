@echo off
echo Start the main process
echo Python version use:
python -V
echo the script is launching ... wait ...
echo %~dp0
pushd %~dp0
python -m main
if errorlevel 1 goto error
pause
goto :eof

:ERROR
echo Continue to install the packages
pause
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pause
echo Continue to launch again main.py
python -m main
pause
goto :eof


