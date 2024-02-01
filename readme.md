# Frequently used commands

initial setup:
mkdir newProject
cd newProject
python3 -m venv env
source env/bin/activate
pip install django  
pip install djangorestframework  
django-admin startproject api .
python manage.py startapp auth

python manage.py makemigrations
python manage.py migrate

Output the list of installed packages and their versions to a file
pip3 freeze > requirements.txt

Install the packages listed in the requirements.txt file
pip3 install -r requirements.txt

docker run -d --rm -p 6379:6379 redis
