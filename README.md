# Test Assignment – Django REST API

This project is developed as part of a backend assessment using
Django and Django Rest Framework.

## Tech Stack

- Python
- Django
- Django Rest Framework
- redis
  

## Setup Instructions

1. Clone the repository

git clone https://github.com/erAsif/test_assignment.git
cd test_assignment

2. Create virtual environment

python -m venv venv

3. Activate virtual environment (Windows)

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Apply migrations

python manage.py makemigrations
python manage.py migrate

6. Run server

python manage.py runserver

## Base URL
admin - http://127.0.0.1:8000/admin/

API - http://127.0.0.1:8000/api/

Swagger - http://127.0.0.1:8000/api/schema/swagger-ui/
 


## Environment file

Create a .env file if required and add your test environment values.


