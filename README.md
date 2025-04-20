# CSDA Pre-Course Assessment

### Database setup
* ```cd workshop01```
* ``python manage.py migrate``
* Populate `polls_quote` table with quotes to choose from

### Env variables
* Create `workshop01/.env`
* Generate and add `SECRET_KEY` value for Django

### Local deployment - Django development server
```python manage.py runserver```

### Local deployment - gunicorn
```gunicorn --bind :8000 mysite.wsgi ```

### GCP deployment
```gcloud app deploy```

### fly.io deployment
```fly deploy```