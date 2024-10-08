#!/bin/bash
source variables.env

echo "Starting Floodlight container..."
sudo docker start $FLOODLIGHT_CONTAINER

sleep 3

echo "Running Mininet Python script..."
sudo python3 $MININET_SCRIPT_PATH

echo "Cleaning up Mininet!"
sudo mn -c

echo "Stopping Floodlight container..."
sudo docker stop $FLOODLIGHT_CONTAINER

echo "Done!"
