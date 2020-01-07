[![CircleCI](https://circleci.com/gh/valentinburk/operationalize-machine-learning-microservice.svg?style=svg)](https://circleci.com/gh/valentinburk/operationalize-machine-learning-microservice)

This is a project for [Cloud DevOps Engineer Nanodegree](https://www.udacity.com/course/cloud-dev-ops-nanodegree--nd9991).

## Project Overview

This project is using a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). 

The project is a Python Flask application. May be run in local Docker infrastructure or deployed to a Kubernetes cluster both local and on-cloud.

### Project Files

* An `sklearn` model pre-trained to predict housing prices in Boston (`housing.csv`, `boston_housing_prediction.joblib`)
* A Python Flask application that acts as a Machine Learning Microservice API for the data (`app.py`, `requirements.txt`)
* A Linux Makefile to prepare the development environment, and to test and lint the source files (`Makefile`)
* A Dockerfile to create a Docker container of the Machine Learning Microservice API (`Dockerfile`)
* A shell script to automate generation of the Docker container (`run_docker.sh`)
* A shell script to automate uploading of the container to Docker Hub (`upload_docker.sh`)
* A shell script to download the container from Docker Hub and deploy it into a Kubernetes environment (`run_kubernetes.sh`)
* A configuration file for [CircleCI](https://circleci.com/)
* Files showing the output of the application (`docker_out.txt`, `kubernetes_out.txt`)
* This `README.md` file

## Setup the Environment

* Create a virtualenv and activate it: For Windows `python -m venv .devops` then `. .devops/Scripts/activate`
* Run `make install` to install the necessary dependencies

### Running `app.py`

1. Standalone:  `python app.py`
2. Build and Run in Docker:  `./run_docker.sh`
3. Publish image to Docker Hub: `./upload_docker.sh`
4. Run in Kubernetes:  `./run_kubernetes.sh`

Running the script `./make_prediction.sh` will perform a test request to the app. This will work with all modes: standalone, docker, k8s.

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Run via kubectl