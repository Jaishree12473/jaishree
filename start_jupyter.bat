@echo off
cd /d "%~dp0"
echo Starting Jupyter Notebook for JAISSHREEPROJECT...
call .venv\Scripts\jupyter.exe notebook JAISSHREEPROJECT.ipynb
pause
