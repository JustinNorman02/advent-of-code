@echo off
:: Check if enough arguments are provided
if "%~1"=="" (
    echo Please provide the parent folder name.
    exit /b
)

if "%~2"=="" (
    echo Please provide the number of folders to check.
    exit /b
)

:: Assign arguments to variables
set parentFolder=%~1
set numberOfFolders=%~2

:: Path to the template file (replace with the actual path to your template.py)
set templateFile=template.py

:: Check if the template file exists
if not exist "%templateFile%" (
    echo Template file not found: %templateFile%
    exit /b
)

:: Check if the parent folder exists
if not exist "%parentFolder%" (
    echo Parent folder "%parentFolder%" does not exist. Exiting...
    exit /b
)

:: Loop through the numbers 1 to the specified number of folders
for /L %%i in (1, 1, %numberOfFolders%) do (
    :: Check if the numbered folder exists
    if exist "%parentFolder%\%%i" (
        echo Checking folder %%i...

        :: Check if the test.txt file exists inside the folder
        if not exist "%parentFolder%\%%i\test.txt" (
            echo Creating test.txt in folder %%i...
            echo. > "%parentFolder%\%%i\test.txt"
        ) else (
            echo test.txt already exists in folder %%i.
        )

        :: Check if the data.txt file exists inside the folder
        if not exist "%parentFolder%\%%i\data.txt" (
            echo Creating data.txt in folder %%i...
            echo. > "%parentFolder%\%%i\data.txt"
        ) else (
            echo data.txt already exists in folder %%i.
        )

        :: Check if the Python template files exist inside the folder
        if not exist "%parentFolder%\%%i\%%i-1.py" (
            echo Copying template.py to %%i-1.py...
            copy "%templateFile%" "%parentFolder%\%%i\%%i-1.py" > nul
        ) else (
            echo %%i-1.py already exists in folder %%i.
        )

        if not exist "%parentFolder%\%%i\%%i-2.py" (
            echo Copying template.py to %%i-2.py...
            copy "%templateFile%" "%parentFolder%\%%i\%%i-2.py" > nul
        ) else (
            echo %%i-2.py already exists in folder %%i.
        )
        
    ) else (
        echo Folder %%i does not exist. Skipping...
    )
)

echo Folder structure checked and updated successfully!