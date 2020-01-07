#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
# Build image and add a descriptive tag
docker build --tag valentinburk/flask-prediction:0.1 .

# Step 2: 
# List docker images
docker images --all

# Step 3: 
# Run flask app
docker run -p 8000:80 valentinburk/flask-prediction:0.1