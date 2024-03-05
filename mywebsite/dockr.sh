#!/bin/bash

# Step 1: Create a Dockerfile
echo "Creating Dockerfile..."
cat << EOF > Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run Django's built-in development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EOF

echo "Dockerfile created successfully!"

# Step 2: Build Docker image
echo "Building Docker image..."
docker build -t mywebsite .
echo "Docker image built successfully!"

# Step 3: Run Docker container
echo "Running Docker container..."
docker run -d -p 8000:8000 mywebsite
echo "Docker container running on port 8000!"
