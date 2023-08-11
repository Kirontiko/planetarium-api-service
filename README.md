# Planetarium Api Service

## Check it Out

[Task Manager deployed to render](https://task-manager-n7we.onrender.com)
- Login: ```TestWorker```
- Password: ```testpass123```
## Table of Contents
 1. [Introduction](#introduction)
 2. [Requirements](#requirements)
 3. [Installation](#installation)
 4. [Used technologies](#used-technologies)
 5. [Usage](#usage)
 6. [Endpoints](#endpoints) 
 7. [Screenshots](#screenshots) 


## Introduction
Planetarium Api Service is provided functionality for users of reserving
tickets for different astronomy shows. Admin users can create new or modify 
existed Astronomy shows, adding images for them, Show Themes, Show Sessions, 
Planetarium Domes.


## Requirements
* python 3.8
* pip

## Installation
1. Clone this repository:
    ```https://github.com/Kirontiko/planetarium-api-service.git```
2. Create virtual environment and activate it:
   * Tooltip for windows:
     - ```python -m venv venv``` 
     - ```venv\Scripts\activate```
   * Tooltip for mac:
     - ```python -m venv venv```
     - ```source venv/bin/activate```

3. Install dependencies:
    - ```pip install -r requirements.txt```

4. Apply all migrations in database:
   - ```python manage.py migrate```

5. Create superuser and apply Email and Password
   - ```python manage.py createsuperuser```

6. Start running django server using this command:
   - ```python manage.py runserver```
   - You will see something like this:
   ```
     Watching for file changes with StatReloader
     System check identified no issues (0 silenced).
     July 25, 2023 - 11:54:15
     Django version 4.1, using settings 'config.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.```
7. Done! Server has been started!

## Used technologies
- Django framework
- Django Rest Framework
- SQLite


## Usage
### For users
    1. Reserving tickets for astronomy shows
    2. Only reading all data from endpoints
### For admins
    1. Creating or modifying astronomy shows
    2. Creating or modifying show sessions
    3. Creating or modifying show themes
    4. Creating or modyfying planetarium domes
    5. + all user allowances

## Endpoints
    "show_themes": "http://127.0.0.1:8000/api/planetarium/show_themes/",
    "reservations": "http://127.0.0.1:8000/api/planetarium/reservations/",
    "astronomy_shows": "http://127.0.0.1:8000/api/planetarium/astronomy_shows/",
    "planetarium_domes": "http://127.0.0.1:8000/api/planetarium/planetarium_domes/",
    "show_sessions": "http://127.0.0.1:8000/api/planetarium/show_sessions/"

## Screenshots

### DB Schema
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/7442b3ac-7809-4e30-b08c-f5ea6b4fb777)

### Swagger
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/78e6d90c-06c0-4fb0-8ae7-44d09ea8db1e)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/d685095f-26ee-4a59-b1bf-3471bce1b8ca)
### Show Themes

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/9fd2b8e3-8db5-4217-9f93-c2cd9d826a4f)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/80f81974-1667-4da1-9ea2-db1167423965)

### Reservation
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/af19419b-094a-4526-8f0e-eb130b4b9dc7)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/8f813d30-107c-4a2c-baef-3e132ac01ebf)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/ff41414a-2478-4ee1-b4dd-66fc9d483434)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/bcc342f8-6ae8-406c-b9a5-6744b40f7b3b)

### Astronomy Shows

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/4f304a54-55ea-4ce3-9564-876707f63994)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/0736dba4-fdb5-4055-bff9-b5821225aa73)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/99122ee9-87d9-4e0d-a8d1-7a922b9a2e53)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/ec896cd8-1dde-45c9-9b2b-5d192862bfda)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/a6720a31-1507-4ca8-bbbe-4afcc37e750b)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/4b2ff705-42f3-4280-888e-50753b40a3f3)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/66735d70-6ee9-4e14-9439-388a1fdda062)


### Planetarium Domes

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/5f1a4f30-9da5-49fc-adc5-d45156ab25b1)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/1cbe1064-cc15-4579-8366-552df762832a)



### Show Sessions
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/d1f76a6a-d5ff-4a0c-bf6b-41f1c06a0b84)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/a53670c8-6887-4a68-a0d8-2b94af1d4376)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/87a93bdd-cbaf-4e60-a3c4-e18323ff9cdc)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/d6c6e85e-8f8a-4ee6-b911-d420c3f1dde2)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/f99f19d5-7645-4787-96fe-524e74069b9a) 
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/f649b7da-0ac6-4d2b-af9b-505ce9ebde6d)
