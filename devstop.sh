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