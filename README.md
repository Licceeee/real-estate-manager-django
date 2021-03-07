# real-estate-django
Real estate manager

clone

```git clone https://github.com/Licceeee/real-estate-manager-django.git```

change dir

```cd real-estate-django```

create venv

```virtualenv -p python3 venv```

activate venv

```source venv/bin/activate```

install dependencies

```pip install -r req.txt```

migrate db

```python3 manage.py makemigrations```
```python3 manage.py migrate```

go to project/settings.py and comment out:
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static')
]
```
Comment back in in production mode!

apply static files

```python3 manage.py collectstatic```

 ... IN PROGRESS ...
