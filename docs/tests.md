Running tests in tests.py
```
python manage.py test polls
```

Django test client

used for testing the view

```python
# set up env 
from django.test.utils import setup_test_environment
setup_test_environment()

# import client
from django.test import Client
client = Client()

# get a response from '/'
response = client.get("/")

response.status_code

# we'll use 'reverse()' rather than a hardcoded URL
from django.urls import reverse
response = client.get(reverse("polls:index"))
response.status_code
200
```

