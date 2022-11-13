django install
```
python -m venv venv
source ./venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

django init
```
python manage.py migrate
```

```
python manage.py createsuperuser 
```


update schema
```
python manage.py makemigrations
```

deploy
```
python manage.py migrate
python manage.py runserver

```