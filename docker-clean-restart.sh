# This file is used to do quick clean of the docker setup including the volumes
# mainly used to test docker changes
docker-compose down
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)
sh $1
