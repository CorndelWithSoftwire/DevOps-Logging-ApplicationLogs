# Module 13.1 Application Logs
# Integration With Containers

## Installation Requirements
* Docker desktop

## Running Instructions
To run in docker, run
 
```
$ docker build -t flask-app .   
$ docker run --detach --publish 8000:80 flask-app
```
The app will now be running at 127.0.0.1:8000

## To push container to repo:
```
$ docker tag flask-app {ECR_REPOSITORY_URL}:flask-app
$ docker push {ECR_REPOSITORY_URL}:flask-app
```