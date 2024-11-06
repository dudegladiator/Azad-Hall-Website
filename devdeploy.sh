#!/bin/bash

# Function to check if a command was successful
check_command() {
    if [ $? -ne 0 ]; then
        echo "Error: $1 failed"
        exit 1
    fi
}

# Stop specific Docker containers
echo "Stopping Docker containers..."
docker stop azad_django

# Remove specific Docker containers
echo "Removing Docker containers..."
docker rm azad_django

# Remove associated Docker images
echo "Removing Docker images..."
docker rmi -f azad_django

# Remove unused Docker volumes
echo "Removing unused Docker volumes..."
docker volume prune -f

# Remove unused Docker networks
echo "Removing unused Docker networks..."
docker network prune -f

# Prune unused Docker resources
echo "Pruning unused Docker resources..."
docker system prune -a -f --volumes

# Build the Docker image
echo "Building Docker image..."
docker build --tag azad_django .
check_command "Building Docker image"

# Run the Docker container
echo "Running Docker container..."
docker run -d --name azad_django -p 10000:10000 azad_django
check_command "Running Docker container"

# Wait for the container to start
echo "Waiting for the container to start..."
sleep 5

# Check if the container is running
if [ "$(docker inspect -f '{{.State.Running}}' azad_django)" = "true" ]; then
    echo "Container is running successfully."
    echo "You can access the website at http://localhost:10000"
    echo "To view logs, use: docker logs azad_django"
    echo "To stop the container, use: docker stop azad_django"
else
    echo "Error: Container failed to start. Check the logs with: docker logs azad_django"
    exit 1
fi