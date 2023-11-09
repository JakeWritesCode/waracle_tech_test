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

TODO: Finish README