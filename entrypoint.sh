#!/bin/bash

source $HOME/geo_exercise.env

set -euo pipefail

WAIT_FOR_POSTGRES=${WAIT_FOR_POSTGRES:-true}

if [[ "$WAIT_FOR_POSTGRES" = true ]]; then
    DATABASE_URL=${DATABASE_URL:-postgres://admin:admin@database:5432/geodjango}

    # convert to connection string
    POSTGRES_URL=${DATABASE_URL%%\?*}
    POSTGRES_URL=${POSTGRES_URL/#postgis:/database:}


    # let postgres and other services to warm up....
    until psql $POSTGRES_URL -c '\q'; do
        >&2 echo "**** Postgres database is not available - sleeping"
        sleep 3
    done
fi

if [[ $# -ge 1 ]]; then
    exec "$@"
else
    echo "Applying migrations"

    # migrations
    python manage.py makemigrations
    python manage.py migrate

    # populate database with initial data
    python manage.py populate_db fixtures/countries_initial_data.csv "4326"

    echo "Starting server"

fi
    exec python manage.py runserver 0.0.0.0:8990

