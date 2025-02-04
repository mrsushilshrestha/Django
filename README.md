# Setting Up a Virtual Environment for Django

## 1. Install `virtualenv` (if needed)
If you don't have `virtualenv` installed, run:
```
pip install virtualenv
```

## 2. Create a Virtual Environment
Navigate to your project folder and create the virtual environment:
```
python -m venv virtualenvironment
```

## 3. Activate the Virtual Environment
- **Windows (CMD):**
  ```
  virtualenvironment\Scripts\activate
  ```
- **Git Bash or MINGW64:**
  ```
  source virtualenvironment/Scripts/activate
  ```
- **macOS/Linux:**
  ```
  source virtualenvironment/bin/activate
  ```

After activation, your terminal prompt should show the virtual environment name.

## 4. Install Django and Other Dependencies
To install Django in the virtual environment:
```
pip install django
```

## 5. Common Packages for Django Projects
If your project requires additional packages, install them:
- **Database (PostgreSQL):**
  ```
  pip install psycopg2
  ```
- **Django REST Framework (for APIs):**
  ```
  pip install djangorestframework
  ```
- **Image Handling (Pillow):**
  ```
  pip install pillow
  ```

## 6. Generate a `requirements.txt` File
To keep track of installed packages:
```
pip freeze > requirements.txt
```

## 7. Install Packages from `requirements.txt`
To install all dependencies from the `requirements.txt` file:
```
pip install -r requirements.txt
```

## 8. Deactivate the Virtual Environment
When done, deactivate the virtual environment with:
```
deactivate
```

## Troubleshooting Reminder
- **Command not found:** If you get an error like `bash: script: command not found`, make sure you’re using the correct command syntax:
  - Activate (Git Bash): `source virtualenvironment/Scripts/activate`
- **Missing packages:** Always use `pip install -r requirements.txt` to reinstall all dependencies.
- **Path issues:** Double-check the folder and file paths; they are case-sensitive on some systems.

---

## Additional Notes

### Bypass Windows Security
Run this command to enable script execution in PowerShell:
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Create Virtual Environment
```
pip install virtualenv
python -m venv virtualenvironment
```

### Install Django
```
pip install Django
```

### Check Installed Packages
```
pip list
```

### Create a Django Project
```
django-admin startproject firstProject .
```

### Create a Django App
To create a new app within your project:
```
python manage.py startapp <app_name>
```

### Know Shortcuts for Django Commands
To view available shortcuts and commands:
```
python manage.py
```

### Run the Server
```
python manage.py runserver
```

### Using Django to Render HTML Files

#### Import `HttpResponse`
```python
from django.http import HttpResponse
```

#### For Rendering HTML Files
```python
from django.shortcuts import render 
```

#### Add Templates Directory to `settings.py`
```python
TEMPLATES = [
    {
        'DIRS': ['templates'],
    }
]
```

### Django's Static Image Handling

#### Steps to Make This Work:

1. **Enable Static Files:**
Ensure your `settings.py` file has `STATIC_URL` and `STATICFILES_DIRS` properly configured.
```python
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

2. **Store the Image in the Static Folder:**
Place the image in a directory like `static/image/image-1.png`.

3. **Load Static in the Template:**
At the top of your HTML template:
```html
{% load static %}
```

4. **Updated `<img>` Tag:**
```html
<img src="{% static 'image/image-1.png' %}" alt="My Photo" />
```

---

## Models in Django

```python
from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Override the __str__ method to return a more useful string
    def __str__(self):
        return f"Account(id={self.id}, email={self.email}, username={self.username}, create_at ={self.create_at})"
```

## ORM in Django

### First, Open the Django Shell
```
python manage.py shell
```

### Basic ORM Commands
```python
from app_name.models import class_name
# Example:
from account.models import Account

Account.objects.all()  # View all data in the database
Account.objects.first()  # Return the first data entry
Account.objects.last()  # Return the last data entry
Account.objects.all().count()  # Return total count of data

# Create a new entry
Account.objects.create(email="mrsushilshrestha@gmail.com", username="mrsushilshrestha", password="admin")

# Delete the last entry
Account.objects.last().delete()

# Retrieve data with specific ID
Account.objects.get(id=1)

# Filter data by username
Account.objects.filter(username="sushil")  # Return all matching entries

# Check if data exists
Account.objects.exists()  # Returns True or False
```
