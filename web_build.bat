@echo off
echo Building the Imposter Game for Web (Mobile PWA)...
pip install -r requirements.txt
python -m flet build web
echo.
echo Build complete! 
echo Check the 'build/web' folder.
echo.
echo To run it on your phone:
echo 1. Upload everything inside 'build/web' to a site like GitHub Pages or Vercel.
echo 2. Open the URL in Safari (iPhone) or Chrome (Android).
echo 3. Tap "Add to Home Screen".
pause
