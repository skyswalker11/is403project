# IS403FinalProject
Our IS403 Final Project.

Virtual Environment setup
python -m venv ./venv 
./venv/Scripts/activate.bat       #Start
./venv/Scripts/deactivate.bat     #Stop

Project Setup
Windows:
python -m django startproject {Name_here}
Mac:
python3 -m django startproject {Name_here}

App Setup:
django-admin startproject {Directory}

Run:
python manage.py runserver

Create Super-User:
python manage.py createsuperuser