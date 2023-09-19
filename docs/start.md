1. Install Python and Django following the [doc](https://docs.djangoproject.com/en/4.2/intro/install/)

1. create virtual [env](https://stackoverflow.com/questions/17769430/command-django-admin-py-startproject-mysite-not-recognized)

```bash 
python -m venv venv

venv\Scripts\activate

pip install django
```

3. create django project named mysite
```bash
django-admin startproject mysite
```

4. go into the project directory then run local dev server
```
python manage.py runserver
```