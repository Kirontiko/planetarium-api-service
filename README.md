# Planetarium Api Service

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
### For local running
* python 3.8
* pip

### For running from docker
* Docker

## Installation
1. Clone this repository:
    ```https://github.com/Kirontiko/planetarium-api-service.git```

 2. Create .env file and define environmental variables following .env.example:
    ```
    DEBUG=True|False
    SECRET_KEY=your django secret key
    POSTGRES_HOST=your db host
    POSTGRES_DB=name of your db
    POSTGRES_USER=username of your db user
    POSTGRES_PASSWORD=your db password
    ```
 ### 3. To run it locally
1. Create virtual environment and activate it:
   * Tooltip for windows:
     - ```python -m venv venv``` 
     - ```venv\Scripts\activate```
   * Tooltip for mac:
     - ```python -m venv venv```
     - ```source venv/bin/activate```

2. Install dependencies:
    - ```pip install -r requirements.txt```
3. Apply all migrations in database:
   - ```python manage.py migrate```
4. Run server
   - ```python manage.py runserver```
5. Create admin user
   - ```python manage.py createsuperuser```

### 3. To run it from docker
1. Run command:
      ```
      docker-compose up --build
      ```
### 4. App will be available at: ```127.0.0.1:8000```



## Used technologies
- Django framework
- Django Rest Framework
- PostgreSQL
- Docker


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

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/80f81974-1667-4da1-9ea2-db1167423965)

### Reservation
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/bcc342f8-6ae8-406c-b9a5-6744b40f7b3b)

### Astronomy Shows

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/4f304a54-55ea-4ce3-9564-876707f63994)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/0736dba4-fdb5-4055-bff9-b5821225aa73)


### Planetarium Domes

![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/5f1a4f30-9da5-49fc-adc5-d45156ab25b1)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/1cbe1064-cc15-4579-8366-552df762832a)



### Show Sessions
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/d1f76a6a-d5ff-4a0c-bf6b-41f1c06a0b84)
![image](https://github.com/Kirontiko/planetarium-api-service/assets/90575903/87a93bdd-cbaf-4e60-a3c4-e18323ff9cdc)
