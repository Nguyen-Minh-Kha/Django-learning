> The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

> The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

create a package
```
python manage.py startapp polls
```

> Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

* mysite is website consisting of apps. Polls is an app of mysite

> A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

* each app needs their own urls and these urls can be included in the main "mysite urls"

> The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.



