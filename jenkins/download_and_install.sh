#!/bin/bash

container_name=$('own-external-ip-address')
directory=$('own-external-ip-address')

# Check if the container already exists and running
if docker ps -a --format '{{.Names}}' | grep -q $container_name; then
    echo "Container '$container_name' already exists."

    # Check if the container is running
    if docker ps --format '{{.Names}}' | grep -q $container_name; then
        echo "Container is running, using existing container..."
        CONTAINER_ID=$(docker ps --format '{{.ID}}' --filter "name=$container_name")
    else
        echo "Container is not running, starting it..."
        docker start $container_name
        CONTAINER_ID=$(docker ps --format '{{.ID}}' --filter "name=$container_name")
    fi
else
    echo "Container 'container_name' does not exist, creating it..."
    docker run --rm -d --name $container_name --privileged --entrypoint /bin/bash arm32v7/ubuntu:latest
    CONTAINER_ID=$(docker ps --format '{{.ID}}' --filter "name=$container_name")
fi

# Install necessary packages if they are not installed
echo "Installing necessary packages..."
docker exec $CONTAINER_ID bash -c 'which node npm python3 pip3 tsc curl wget' > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing necessary packages..."
    docker exec $CONTAINER_ID bash -c 'which python3' > /dev/null 2>&1 || docker exec $CONTAINER_ID apt-get install -y python3
    docker exec $CONTAINER_ID bash -c 'which pip3' > /dev/null 2>&1 || docker exec $CONTAINER_ID apt-get install -y python3-pip
    docker exec $CONTAINER_ID bash -c 'which curl' > /dev/null 2>&1 || docker exec $CONTAINER_ID apt-get install -y curl
    docker exec $CONTAINER_ID bash -c 'which wget' > /dev/null 2>&1 || docker exec $CONTAINER_ID apt-get install -y wget
    docker exec $CONTAINER_ID apt-get install -y --upgrade setuptools
    docker exec $CONTAINER_ID pip show scapy &>/dev/null || docker exec $CONTAINER_ID pip install scapy
else
    echo "Necessary packages are already installed."
fi
docker exec $CONTAINER_ID apt-get update -y
docker exec $CONTAINER_ID apt-get upgrade -y

docker exec $CONTAINER_ID /bin/bash -c "export DISPLAY=\$(cat /etc/resolv.conf | grep nameserver | awk '{print \$2}'):0"

if docker exec $CONTAINER_ID ls $directory &> /dev/null; then
    echo "Anemometer is already cloned in the container."
else
    echo "Cloning Anemometer repository..."
    docker exec $CONTAINER_ID git clone https://github.com/jonathan-99/anemometer.git $directory
fi

# Print OS version
echo "OS Version:"
docker exec $CONTAINER_ID cat /etc/os-release

# Print Python version
echo "Python Version:"
docker exec $CONTAINER_ID python3 --version

# Print unittest version
echo "unittest Version:"
docker exec $CONTAINER_ID python3 -m unittest

# Print coverage version
echo "coverage Version:"
docker exec $CONTAINER_ID coverage --version

# Print Docker image ID
echo "Docker Image ID:"
docker exec $CONTAINER_ID cat /proc/self/cgroup | grep "docker" | sed 's/^.*\///' | head -n 1


