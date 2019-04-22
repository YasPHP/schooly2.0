#!/bin/bash

# Waits until Postgres DB is accessible (started in different container)
#while ! curl http://$DB_HOST:$DB_PORT/ 2>&1 | grep '52'
#    do
#        echo 'retry'
#        sleep 5
#    done
sleep 30

if [ $ENV == "DEV" ]; then
    # We are in development mode
    # Start the server with Django's debugging built-in server
    python3 manage.py runserver 0.0.0.0:80 &
else
    # We are in production mode
    # Start the server using gunicorn, b/c more robust for production
    gunicorn iyna.wsgi:application -b :80 &
fi

# Make migrations and apply them to the database
python /code/manage.py makemigrations
python /code/manage.py migrate

# Collect any static files
python /code/manage.py collectstatic --noinput --verbosity 0

# Essentially just let the web server run. If we don't have this, it will exit out.
sleep infinity