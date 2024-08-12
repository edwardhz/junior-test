# IMPORTANT NOTE
I've solved all the points with all the bonuses, I had to make a workaround to get the nginx service available outside the kubernetes cluster, but it works. I also used DockerHub images from my repo to build the kubernetes objects.

# Project Overview

This project contains a backend application, database configuration, Docker compose configuration, Kubernetes deployment files, and Nginx setup. Below is the structure of the project directory and the function of each file and folder.

## Folder Descriptions

- **Backend/**: Contains the backend application code, dependencies, and Dockerfile to build the backend image.
- **db/**: Contains the SQL schema file and Dockerfile for setting up the database.
- **k8s/**: Contains Kubernetes deployment and service configurations for the backend, database, and Nginx.
- **mysql_data/**: Directory used for MySQL data persistence.
- **nginx/**: Contains the Nginx Dockerfile and configuration file.
- **docker-compose.yaml**: Used to orchestrate the backend, database, and Nginx containers.

## How to Use

- **Docker Compose**: Go to the root folder project/ and rum the docker compose orchestation then you can use http://localhost/list or http://localhost/hello with json encoded, the petitions will go through the nginx.
- **Kubernetes (Minikube)**: Go to k8s/ and start minikube using *minikube start*, apply the name space first *kubectl apply -f namespace.yaml* then apply all  *kubectl apply -f .*. We'll access the nginx through a NodePort service, but we can't do that directly with minikube, so we have to use *service nginx-service -n junior-test --url* to provide a link to our service running inside the Kubernetes cluster, then we can perfom the same requests on the IP and port given by the command from our machine. Example : http://127.0.0.1:36499/list or http://127.0.0.1:36499/hello with enconded json. (only accepts POST methods)


