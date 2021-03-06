#!/bin/bash

until bash -c "flask db current"; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up, starting zadacha"
flask db upgrade
gunicorn run:app -b 0.0.0.0
