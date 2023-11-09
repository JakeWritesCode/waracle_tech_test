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
cd <project root>/docker
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
You can see the pipeline here: https://app.circleci.com/pipelines/github/JakeWritesCode/waracle_tech_test

To speed up testing I have added factory-boy to the requirements. Factory-boy is a great library for 
standardising creating test model data. You can see an example in `cake/tests/factories.py`.

## Linting and formatting

Linting and formatting is covered by the excellent Ruff library. I have also configured pre-commit hooks to run
linting and formatting on every commit. To run the linter and formatter manually, run the following command:

```shell
cd <project root>
ruff format .
ruff lint .
```

## API Documentation

API documentation is created in OpenAPI/Swagger 3.0 format. You can view the docs by running the app and visiting
http://localhost:8000/api/docs/. 

I have also installed drf-spectacular, which does a reasonable job of automating the documentation.

With a bit more time, contract testing for the endpoints back to the OpenAPI spec would be a nice addition.

The YAML file is also directly accessible at http://localhost:8000/static/schema.yaml



## Deployment
The requirements documentation for this test stated: 

> The API should be deployed to Docker or Kubernetes, onto whatever solution you like, impress us.

I have provided the local development environment in docker-compose, and am quite happy to talk you through 
how I would deploy this in production using NGINX and Gunicorn. Given the simplicity of the app, a full kubernetes
deployment seems like overkill. I would possibly aim for a simpler deployment with something like google app engine, 
AWS lightsail or even Heroku.

I hope all this makes sense! Please let me know if you have any questions.

