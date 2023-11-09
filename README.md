# Waracle API Test

My implementation of the Waracle API Tech test. This project is intended to mirror a production project as far as
reasonably possible. I've chosen to build the API in Django and DRF as I'm most familiar with this stack and
it matches the required skills for the job description.

In addition to the required functionality I've added a few extras, intended to improve quality, developer experience
and match production standards. These include:

- Dockerised development / deployment environment
- Option for localised development environment
- Test suite and basic CI pipeline implemented with CircleCI.
- FactoryBoy for test data generation.
- Linting and formatting using the excellent Ruff library, including pre-commit hooks.
- API documentation using Swagger.
- Configuration mapped to environment variables.

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


## Testing

Tests are configured to run in pytest. To run the tests, run the following command:

```shell
cd <project root>
source development_envvars.sh
pytest .
```

I have also configured a CI pipeline using CircleCI. This will run the tests and linting on every commit.
