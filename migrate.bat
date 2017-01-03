@echo off

python manage.py makemigrations comment_scraper
python manage.py migrate
pause
