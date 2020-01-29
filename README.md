# treez
Treez technical assessment

## Database models
Can be found in order_app/models
Migrations for these models can be found in order_app/migrations  
This folder shows how the models are changed over time after creation to 
fit new requirements or change structure

## Requirments
This project is build with python3 and Django 3 
Virtualenv is recommended to save packages to the local project instead of polluting global
```
sudo apt install virtualenv
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Tests

## Running
Run with `python manage.py runserver --settings=treez.settings`  
View `localhost:8000` to explore the api
