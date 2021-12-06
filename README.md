# Lunar Phase

Lunar Phase is a django based web application, to generate current day lunar phase. The project is dockerised for both dev and production environment.

## Details of the Project

The project has two pages,
1. Login Page (Takes username and password of the user)
2. Dashboard (Provide details of the current day moon phase)

The data provided on the moon phase dashboard :
1. Days since known new moon (From 1/6/2000 at 12:24:01)
2. Nth moon cycle
3. Progress of current moon cycle
4. Current stage of the moon
5. Moon phase illustration

## Techstack of the Project
1. Django==3.2.6
2. psycopg2-binary==2.9.1
3. gunicorn==20.1.0 (For Prod env)
4. Nginx (For Prod env)

## Prerequisites
Should have Docker version <= 20.10.7 and docker-compose version <= 1.17.1  installed on the machine 

## Usage
```console
foo@bar:~$ git clone https://<username>@bitbucket.org/dheeraj10/safeex.git

foo@bar:~$ sh auto_run.sh # This will run the server in development environment

```

auto_run.sh takes one optional argument "prod"
```console
foo@bar:~$ sh auto_run.sh prod # This will run the server in production environment

```
When running on production environment, the application will be served using guincorn and nginx.


## Sample Images
### Login Page
![Login Page](https://i.ibb.co/C5PHGh1/login.png "Login Page")

### Dashboard Page
![Dashboard Page](https://i.ibb.co/Xkw5vPZ/dashboard.png "Dashboard Page")


Happy Hacking !!!