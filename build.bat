@echo off
echo Building the Imposter Game executable...
pip install -r requirements.txt
pip install pyinstaller
flet pack main.py --name "Imposter_Game"
echo Build complete! Check the dist/ folder for Imposter_Game.exe
pause
