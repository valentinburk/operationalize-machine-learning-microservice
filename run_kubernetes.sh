#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=valentinburk/flask-prediction:0.1

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run flask-prediction --image=${dockerpath} --labels="tag=udacity"

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
POD_NAME=$(kubectl get pods -l tag=udacity -o jsonpath='{.items[0].metadata.name}')
kubectl port-forward "${POD_NAME}" 8000:80