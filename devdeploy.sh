#!/bin/bash

# Check if cloudflared is installed
if ! command -v cloudflared &> /dev/null; then
    echo "Performing initial setup..."
    
    # Update and upgrade the system
    sudo apt update && sudo apt upgrade -y

    # Install essential tools and libraries
    sudo apt install -y apt-transport-https ca-certificates curl software-properties-common \
        git vim nano tmux neofetch htop tree unzip wget \
        build-essential python3 python3-pip nodejs npm 

    # Install Docker
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg.tmp
    sudo mv -f /usr/share/keyrings/docker-archive-keyring.gpg.tmp /usr/share/keyrings/docker-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt update 
    sudo apt install -y docker-ce docker-ce-cli containerd.io

    # Add user to docker group
    sudo usermod -aG docker $USER

    # Install Docker Compose
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    # Install cloudflared
    sudo mkdir -p --mode=0755 /usr/share/keyrings
    curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null

    echo "deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflared.list

    sudo apt-get update && sudo apt-get install cloudflared

    # Install NVM (Node Version Manager)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

    # Load NVM
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

    # Install latest LTS version of Node.js
    nvm install --lts

    # Install some global npm packages
    npm install -g yarn typescript ts-node

    # Setup a basic .tmux.conf file
    echo "set -g mouse on" > ~/.tmux.conf
    echo "set -g history-limit 10000" >> ~/.tmux.conf

    # Verify installations
    echo "Docker version:"
    docker --version
    echo "Docker Compose version:"
    docker-compose --version
    echo "Python version:"
    python3 --version
    echo "Node.js version:"
    node --version
    echo "npm version:"
    npm --version
    echo "cloudflared version:"
    cloudflared --version

    # Run neofetch to display system info
    neofetch

    echo "Setup complete! Please log out and log back in for all changes to take effect."
else
    echo "Initial setup already done (cloudflared is installed), skipping..."
fi

# Rest of your script continues here...
rm -rf ./cloudflared_10000.log

# Function to start a cloudflared tunnel and extract the URL
start_tunnel() {
    local port=$1
    local log_file="cloudflared_${port}.log"
    cloudflared tunnel --url http://localhost:$port > $log_file 2>&1 &
    local pid=$!
    
    # Wait for the URL to appear in the log file (timeout after 30 seconds)
    local timeout=30
    local url=""
    while [ $timeout -gt 0 ] && [ -z "$url" ]; do
        url=$(grep -o 'https://.*\.trycloudflare.com' $log_file)
        if [ -z "$url" ]; then
            sleep 1
            ((timeout--))
        fi
    done

    if [ -n "$url" ]; then
        echo "$url:$pid"
    else
        echo "Failed to get URL:$pid"
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

# Run the Docker container
echo "Running Docker container..."
docker run -d --name azad_django -p 10000:10000 azad_django

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

backend_result=$(start_tunnel 10000)
backend_pid=$(echo $backend_result | cut -d':' -f2)

echo "Backend cloudflared : $backend_pid"