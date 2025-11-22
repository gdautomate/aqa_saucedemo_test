@echo off
echo Running tests...
mkdir reports 2>nul
pip install -r requirements.txt
pytest -m "success or failed or extract" --html=reports/report.html --self-contained-html
pause
