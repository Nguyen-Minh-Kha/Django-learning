run migration 
```
python manage.py migrate
```

> The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app

--- 

models creation

* each model is a class in the models.py file

> each model is represented by a class that subclasses django.db.models.Model

---

make migration file

```
python manage.py makemigrations <name of the app in apps.py AppConfig>
```

preview the sql executed for migration
```
python manage.py sqlmigrate polls 0001
```



```
remember the three-step guide to making model changes:

1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.
```