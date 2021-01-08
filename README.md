# Emerging Technology Project 2020 - G00354922
### Using python to produce a model that accurately predicts wind turbine power output from wind speed values.

## Introduction / Project Description
As part of the Emerging Technology module in 4th year, we were tasked to create a web service that uses machine learning to make predictions based on a "powerproduction" data set which we were povided with. 
- This project contains a jupyter notebook that trains a model using the "powerproduction" dataset. The notebook explains how the code works as well as providing a physical view of the model.
- Python script that runs the web service based on the model. This web service allows the user to provide a value for speed and returns the estimated power value according the the model.
- a Dockerfile which is used to build and run the web service in a container

## Run the web service using docker
docker build -t myapp
docker run -d -p 5000:5000 myapp

note: 'myapp' can be replaced with another name if desired

## Run the web service without docker
- open CMD
- Type: "export FLASK_APP=WebService.py"
- Type: "flask run"
 * Open Browser on "http://127.0.0.1:5000/"

## References
All model creation-related references can be found in the jupyter notebook

Python script that runs web service:<br/>
https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html

https://www.freecodecamp.org/news/build-a-simple-json-api-in-python/

Dockerfile to build and run container:<br/>
https://docs.docker.com/compose/gettingstarted/
