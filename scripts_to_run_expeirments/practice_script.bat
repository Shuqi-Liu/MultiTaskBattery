set PYTHONPATH=C:\Users\shl187\Downloads\BrainWalk\MultiTaskBattery\
echo %PYTHONPATH%

C:\Users\shl187\Downloads\BrainWalk\Python390_working\Programs\Python\Python39\python.exe %PYTHONPATH%\experiments\braingait_practice\run_practice.py

if errorlevel 1 (
    echo An error occurred!
    pause
)