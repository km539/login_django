```
python -m pip install djangorestframework
django-admin startproject backend .
python manage.py migrate

python manage.py runserver
```

```sql
CREATE TABLE users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  hashedpassword TEXT NOT NULL,
  salt TEXT NOT NULL
);
```
