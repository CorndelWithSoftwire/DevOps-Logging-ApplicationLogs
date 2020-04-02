# Module 13.1 Application Logs
# Managing/Archiving Logs

## Installation Requirements
* Docker desktop
* AWS CLI

## Running Instructions
To run in docker, run
 
```
$ docker build -t flask-app .   
$ docker run --detach --publish 8000:80 flask-app
```
The app will now be running at 127.0.0.1:8000

## To push container to repo:
First login to AWS:
```
aws ecr get-login-password --region {REGION_NAME} | docker login --username AWS --password-stdin {ECR_ACCOUNT_URL}
```
Next tag and push the container
```
$ docker tag flask-app {ECR_REPOSITORY_URL}:flask-app
$ docker push {ECR_REPOSITORY_URL}:flask-app
```

## To setup AWS stack in CloudFormation
Upload and run cloudformation.yaml