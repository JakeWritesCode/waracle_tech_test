# Waracle API Test

My implementation of the Waracle API Tech test. This project is intended to mirror a production project as far as
reasonably possible. I've chosen to build the API in Django and DRF as I'm most familiar with this stack and
it matches the required skills for the job description.

In addition to the required functionality I've added a few extras, intended to improve quality, developer experience
and match production standards. These include:

- Dockerised development / deployment environment (see [#Docker](#docker))
- Option for localised development environment (see [#Local Development](#local-development))
- Test suite and basic CI pipeline implemented with CircleCI. (see [#Testing](#testing))
- FactoryBoy for test data generation. (see [#Testing](#testing))
- Linting and formatting using the excellent Ruff library, including pre-commit hooks. (
  see [#Linting and Formatting](#linting-and-formatting))
- API documentation using Swagger. (see [#API Documentation](#api-documentation))
- Configuration mapped to environment variables. (see [#Configuration](#configuration))

## Development / Running the app
I have created a dockerised development environment for this project using docker compose, including the following:

 - Django app server (with hot reloading)
   - The venv, code and env variables are shared with the host system,so you can use your IDE of choice to develop.
 - Postgres database (with persistent storage)
 - Swagger UI (for API documentation)

### Running the app in docker
To run the app in docker, you will need to have docker and docker-compose installed. 
To install docker,see: https://docs.docker.com/get-docker/
Once docker is installed, you can run the app with the following command:

```shell
cd <project root>
docker-compose up
```

Then, to navigate to the api docs, visit: http://localhost:8000/api/docs/

Making changes to the code will automatically reload the server.


### Running the app locally
You can also run the app locally. You'll need a few more pre-requisites installed:
- Python 3.10
- Postgres 15
- A postgres database called `waracle_api_test` with a user `postgres` and password `postgres`

Then, to run the app:

    ```shell
    cd <project root>
    source development_envvars.sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/production.txt
    python manage.py migrate
    python manage.py runserver
    ```

Again, to navigate to the api docs, visit: http://localhost:8000/api/docs/

