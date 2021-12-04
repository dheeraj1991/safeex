docker-compose up -d --build

# Initial migration, can be commented out once run
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate

# Create user 
docker-compose exec web python create_user.py
