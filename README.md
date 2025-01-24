# Kafka Tutorial

This is a simple project to demonstrate how to use Kafka in Python.

It is designed to run locally using Docker Compose.

## Prerequisites

- Python 3.10
- Docker Desktop

## Setup

Clone the repo and install the dependencies

Make sure you have the docker container running

NOTE: docker has to be running first before running consumers or producers or they won't work.

Run

```bash
uv run consumer.py
```

to start the consumer

Then start both producers in separate terminals

```bash
uv run producer.py
```

```bash
uv run producer-two.py
```

Optionally you can run a second consumer but this should be enough to get started.
