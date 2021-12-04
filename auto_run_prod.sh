docker-compose -f docker-compose.prod.yml up -d --build

# Initial migration, can be commented out once run
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input --clear

# Create user 
docker-compose exec web python create_user.py
