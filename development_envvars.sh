#A series of development environment variables for the development environment.
#Not to be used in production!

# Add postgres.app to the path so we can build psycopg2 without problems
# Only required for M1 macs on local dev.
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin

export DJANGO_SETTINGS_MODULE="waracle_tech_test.settings.development"
export SECRET_KEY="a_very_insecure_development_secret_key"
export DJANGO_DEBUG=0
export DJANGO_ALLOWED_HOSTS="*"
export DJANGO_DB_HOST="localhost"
export DJANGO_DB_PORT="5432"
export DJANGO_DB_NAME="waracle_tech_test"
export DJANGO_DB_USER="postgres"
export DJANGO_DB_PASSWORD="postgres"