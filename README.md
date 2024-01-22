## Comment 

I selected the FastAPI framework below as it enables easy testing/evaluation through the automated generation 
of an OpenAPI Swagger documentation. Through the Swagger documentation, requests can be send and their
responses can be checked within the browser. 

Being used to the FastAPI framework is another reason why I selected it. This way I could finish the task
faster than if I used another language/framework.

Currently, I do not have the resources to deploy a container, so I would appreciate it if you could follow
the commands below to run the docker container locally and confirm the functionality of the API. However,
deploying the docker container in AWS or GCP should generally not be an issue.


# Temperature API

This API converts temperatures in the Celsius and Fahrenheit scale into each other.

    Language: Python
    Framework: FastAPI

## Requirements (Linux Systems (Ubuntu/WSL))

Before proceeding, ensure you have Docker installed on your system. If not, you can install it using the following command:

    apt-get install docker

## Usage

To start up the container, do the following. 
(sudo is not necessarily required for the next commands, but it enables a quick setup without the need
to worry about permissions. In general, I would not recommend using sudo if not necessary. This time I
made an exception for the task.)

Make sure you are in the base directory: /temperature_api 
    
Start the API docker container using Docker Compose:

    sudo docker compose up --build -d

Once the API container is running, you can access the interactive documentation at http://127.0.0.1/docs.

Stop the API container by:

    sudo docker compose down

Run the test container by (stop the application before running tests):

    sudo docker compose -f docker-compose.test.yml up --build -d

Confirm the output of the test container by:

    sudo docker logs temperature_api-test

Stop the test container with the above command to stop the API container.
    