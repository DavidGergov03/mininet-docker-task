# Mininet + Floodlight Automation

This project automates the setup and running of a Floodlight SDN controller with Mininet using Docker and a custom Python script.

## Prerequisites

- **Docker**: Ensure Docker is installed and running on your system.
- **Mininet**: Install Mininet (must run as root).
- **Python**: Ensure Python 3.x is installed.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/DavidGergov03/mininet-docker-task.git
   cd mininet-docker-task
   
2. Create and configure the .env file:

   ```bash
   cp .env.example .env
   
3. Edit the .env file to match your setup: 

   ```env
   FLOODLIGHT_CONTAINER=floodlight
   MININET_SCRIPT_PATH=/path/to/your/mininet_script.py

## Usage

### Starting the Project:

Run the provided bash script `start_mininet.sh`:

```bash
sudo ./start_mininet.sh
```

This script will:

    Start the Floodlight container using Docker.
    Run your Mininet Python script.
    Open the Mininet interactive UI (if the Python script triggers it).

Exiting Mininet:

Once you are done using the Mininet UI, type exit or press Ctrl+D to close the Mininet interface.

After exiting, the script will:

    Clean up Mininet using sudo mn -c to remove any network configuration.
    Stop the Floodlight Docker container automatically.
