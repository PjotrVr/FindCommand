@echo off
for /f "delims=" %%x in ('powershell -Command "((Get-Content -Path config.json -Raw | ConvertFrom-Json).desiredPath)"') do set desiredPath=%%x
for /f "delims=" %%x in ('powershell -Command "((Get-Content -Path config.json -Raw | ConvertFrom-Json).commandName)"') do set commandName=%%x
setx PATH "%PATH%;%desiredPath%" /M

pip install -r requirements.txt

cd %~dp0
set currentPath=%CD%
set mainPyPath=%currentPath%\src\main.py

echo @echo off > %desiredPath%\%commandName%.bat
echo python "%mainPyPath%" %%* >> %desiredPath%\%commandName%.bat