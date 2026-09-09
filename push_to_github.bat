@echo off
cd /d "%~dp0"
set "PATH=C:\Users\jangi\AppData\Local\Programs\Git\cmd;C:\Users\jangi\AppData\Local\Programs\Git\mingw64\bin;%PATH%"
echo ========================================================
echo Pushing code to https://github.com/Jaishree12473/jaishree.git ...
echo ========================================================
echo.
"C:\Users\jangi\AppData\Local\Programs\Git\cmd\git.exe" push -u origin main
echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo SUCCESS: Pushed to GitHub repository successfully!
    echo ========================================================
) else (
    echo ========================================================
    echo Push did not complete. If prompted, please log in.
    echo ========================================================
)
echo.
pause
