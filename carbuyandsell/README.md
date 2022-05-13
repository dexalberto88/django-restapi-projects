# Development
## Install python3, pip, venv
cd ~
sudo apt update
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate

## Install Django (https://www.djangoproject.com/download/)
pip install Django==4.0.4
python -m django --version

## Create django project (https://docs.djangoproject.com/en/4.0/)
django-admin startproject carbuyandsell
cd carbuyandsell/
python manage.py runserver
or 
python manage.py runserver 0.0.0.0:8000 // in docker

## Create django app
python manage.py startapp carbuyandsellapp

## Install Django rest framework (https://www.django-rest-framework.org/tutorial/quickstart/)
pip install djangorestframework
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
touch carbuyandsellapp/serializers.py

python manage.py startapp restapiapp
pip3 freeze > requirements.txt
pip install tzdata // For docker error 'No time zone found with key UTC'
pip install -r requirements.txt
