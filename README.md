# ModelarDB-RS Pilot
Pilot for the ModelarDB architecture, including a manager node, an edge node, and a cloud node. The following 
repositories are included as git submodules:

1. [ModelarDB-RS](https://github.com/ModelarData/ModelarDB-RS)
2. [Telegraf-Output-Apache-Arrow-Flight](https://github.com/ModelarData/Telegraf-Output-Apache-Arrow-Flight)

Using the individual [Docker](https://www.docker.com/) environments that are included in each repository, this
repository creates a single complete environment to demonstrate the features of the system.

## Setup
Running the pilot can be done exclusively using [Docker](https://docs.docker.com/). Downloading
[Docker Desktop](https://docs.docker.com/desktop/) is recommended, to make maintenance of the created containers easier.
Once [Docker](https://docs.docker.com/) is set up, navigate to the `ModelarDB-RS-Pilot` folder. The
[Docker](https://docs.docker.com/) services for the pilot environment can be built and started using the following command:

```console
docker-compose -p modelardb-pilot up
```

Note that `-p modelardb-pilot` is only used to name the project to make it easier to manage in
[Docker Desktop](https://docs.docker.com/desktop/). Once created, the container can be started and stopped using
[Docker Desktop](https://docs.docker.com/desktop/) or by using the corresponding commands:

```console
docker-compose -p modelardb-pilot start
docker-compose -p modelardb-pilot stop
```

Running the pilot environment starts the services required by ModelarDB to run the full environment with all features 
available. The following table describes the full list of services that are running in the pilot environment.

TODO: Add a table.

## Configuration

TODO: Configure the MQTT broker or topics

TODO: Configure the table that is ingested into

TODO: Configure ModelarDB edge settings (link to documentation).

## Features

TODO: How to ingest with MQTT streamer

TODO: How to ingest normally.

TODO: How to query.
