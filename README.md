# llm-stack

This is a Docker Compose stack for running an LLM (Large Language Model) and a web UI for interacting with it. The stack consists of two services: `ollama` and `open-webui`.

## Prerequisites

- [Docker](https://www.docker.com/get-docker) installed and running on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed and running on your system
- An NVIDIA GPU (for the `ollama` service)
- A directory to store cache files (set the `PATH_CACHE` environment variable)

## Configuration

Before running the stack, make sure to copy the `.env.example` file to `.env` in the root directory and update the variables as needed:

- `PUID`: the user ID to run the containers with
- `PGID`: the group ID to run the containers with
- `TZ`: the timezone to use (e.g. America/Sao_Paulo)
- `PATH_CACHE`: the path to store cache files (e.g. /mnt/cache)
- `GPU_DEVICE_ID`: the ID of the NVIDIA GPU to use (e.g. 0)
- `PORT_WEBUI`: the port to use for the web UI (e.g. 3000)

## Running the stack

To start the stack, run the following command from the root directory:

docker-compose up -d

To access the web UI, open a web browser and go to `http://localhost:3000`.
