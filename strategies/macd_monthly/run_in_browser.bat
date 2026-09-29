@echo off
REM Runs this strategy on its own, in your web browser, without the NIFTY Trader window.
REM Uses the same data folder as the desktop app. Do not run both at once.
cd /d "%~dp0"
set "DATA_DIR=%~dp0data"
python -m pip install --quiet --disable-pip-version-check flask requests
echo Open http://127.0.0.1:5003 in your browser. Leave this window open.
python macd_app.py
pause
