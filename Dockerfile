# Use an official Python runtime as a parent image
FROM --platform=linux/386 python:3.11.4

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get install python3-dev -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt
