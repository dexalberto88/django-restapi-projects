## Development
Install python3, pip, venv and create env
(https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
```bash
sudo apt update
sudo apt install git
sudo apt install python3 python3-pip python3-venv
python3 -m venv env
source env/bin/activate
```

Install Django
(https://www.djangoproject.com/download/)
```bash
pip install Django==4.0.4
python -m django --version
```

Create Django project and app
(https://docs.djangoproject.com/en/4.0/)
```
django-admin startproject carbuyandsell
cd carbuyandsell/
python manage.py runserver # or
python manage.py runserver 0.0.0.0:8000 # in docker
python manage.py startapp carbuyandsellapp
pip install tzdata # For docker error 'No time zone found with key UTC'
```

Install REST Framework
(https://www.django-rest-framework.org/tutorial/quickstart/)
```
pip install djangorestframework
```

Save python libraries
```bash
cd carbuyandsell/
pip freeze > requirements.txt
```

## Usage
```bash
cd ~
git clone https://github.com/dexalberto88/django-restapi-projects.git
cd django-restapi-projects/
python3 -m venv env
source env/bin/activate
cd carbuyandsell/
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py runserver 0.0.0.0:8000
# Open http://172.17.0.2:8000/admin/
# Click Cars and add some entries
# Go to http://172.17.0.2:8000/cars/
# Thats it cheers!
```
