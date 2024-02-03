# Frequently used commands

Initial project `setup`

```bash
mkdir newProject
cd newProject
python3 -m venv env
source env/bin/activate
pip install django djangorestframework
django-admin startproject api .
python manage.py startapp auth
```

## Frequently used python commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Output the list of installed packages and their versions to a file
pip3 freeze > requirements.txt

# Install the packages listed in the requirements.txt file
pip3 install -r requirements.txt

# run docker in detachmode with prot 6379 in both local and docker container with redis database
docker run -d --rm -p 6379:6379 redis
```
