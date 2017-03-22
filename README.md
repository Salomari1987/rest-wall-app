# rest-wall-app

# Wall App Messaging API #

## Start the api (Instructions)
After cloning (or Downloading) the project into your local do from the root repository
* ```cd $repo```
* ```mkvirtualenv rwa```
* ```pip install --upgrade -r requirements.txt```   - to install dependancies
* ```workon rwa``` for any future time
* ```cd wallapp && python manage.py runserver```
* Access api on **localhost:8000**

** Note **: This project works on python 2.7 and Django 10, make sure they are in your path.
** Note **: FrontEnd that consumes this API is at [client-wall-app](https://github.com/Salomari1987/client-wall-app)

## Testing
* all tests are in /api/tests.py folder
* full tests: ```python manage.py test api```

## URLs:
* ```/api/messages GET, POST```
* ```/api/login POST```
* ```/api/register POST```

## Known issues:
* A fake email account was used to send emails to signed up users which can impose a security threat
* Clear text passwords are being received
* Pagination and hyperlinks are not used, GET request to messages can return a huge number of messages if DB is full
* SQLite is used as DB which is not production grade
