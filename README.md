# flight-api
Api to book a flight
[![Maintainability](https://api.codeclimate.com/v1/badges/0a24fa28f6ca291b7f05/maintainability)](https://codeclimate.com/github/kenware/flight-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/kenware/flight-api/badge.svg?branch=staging)](https://coveralls.io/github/kenware/flight-api?branch=staging)
[![CircleCI](https://circleci.com/gh/kenware/flight-api/tree/staging.svg?style=svg)](https://circleci.com/gh/kenware/flight-api/tree/staging)

## Description
Flight-api enables users to to conveniently book a flight any where they are. It contains some features that remind users of there flight schedule

## Installation Guide and Setup
* check that python is installed
    ```bash
    python --V
    ```
* Install Postgres database

* Clone this project
    ```bash
    git clone https://github.com/kenware/flight-api.git
    ```
* Enter project root directory
    ```bash
    cd flight-api
    ```
* install virtual env in your terminal at the project root
    ```bash
    pip install virtualenv
    ```
* Activate virtualenv 
    ```bass
    source .env/bin/activate
    ```
* Install packages
    ```bash
    pip install -r requirements.txt
    ```
* In the root directory, open `env/bin/activate` file and add the environmental variable at the bottom of the `activate` file accordingto the sample bellow:
    ```python
    export DATABASE_NAME=<database_name>
    export DATABASE_USER=<postgres_user>
    export DATABASE_PASSWORD=<postgres password>
    export DATABASE_HOST=localhost
    export DATABASE_PORT=5432
    export SENDGRID_API_KEY=<send_grid_api>
    ```
* Inside the `deactivate` block of code in the `env/bin/activate` file add:
    ```python
    unset DATABASE_NAME
    unset DATABASE_USER
    unset DATABASE_PASSWORD
    unset DATABASE_HOST
    unset DATABASE_PORT
    unset SENDGRID_API_KEY
    ```
* The sample activate file can be found on `sample_env_acivate` file in this project.

* Run test
    ```bash
    python manage.py test
    ```
* Migrate tables to postgres database
    ```bash
    python manage.py migrate
    ```

* Start the application
    ```bash
    python manage.py runserver
    ```

* Start redis server on a new terminal
    ```bash
   redis-server
    ```

* Start celery server on a new terminal
    ```bash
    celery -A flight_control -l info
    ```

## Locust
* Start the application
    ```bash
    python manage.py runserver
    ```

* run locust on another terminal
    ```bash
    locust --host=http://127.0.0.1:8000/
    ```

* open `http://127.0.0.1:8089/` on the browser to see locust interphase. Enter any numbers in the locust form to run on this application

## Documentation
* This API is fully documented using POSTMAN

