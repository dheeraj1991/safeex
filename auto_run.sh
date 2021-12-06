#!/bin/sh

ARG1=${1:-dev}
if [ "$ARG1" = 'prod' ]
then
    docker-compose -f docker-compose.prod.yml up -d --build
else
    docker-compose up -d --build
fi


# Initial migration, can be commented out once run
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate

# Create user 
docker-compose exec web python create_user.py


if [ "$ARG1" = 'prod' ]
then
    docker-compose exec web python manage.py collectstatic
fi