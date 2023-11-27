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

| **Name**              | **Description**                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| minio-server          | [MinIO](https://min.io/) server that functions as the remote object store.                                                                               |
| create-bucket         | [MinIO](https://min.io/) client to initialize the demo bucket `modelardata`.                                                                             |
| postgres              | [PostgreSQL](https://www.postgresql.org/) database used for the cluster metadata database.                                                               |
| modelardb-manager     | ModelarDB manager with an [Apache Arrow](https://arrow.apache.org) Flight interface that can be accessed by sending requests to `grpc://127.0.0.1:9998`. |
| modelardb-edge        | ModelarDB edge with an [Apache Arrow](https://arrow.apache.org) Flight interface that can be accessed by sending requests to `grpc://127.0.0.1:9999`.    |
| modelardb-cloud       | ModelarDB cloud with an [Apache Arrow](https://arrow.apache.org) Flight interface that can be accessed by sending requests to `grpc://127.0.0.1:9997`.   |
| create-table          | Python script in [utility.py](utility.py) used to create the `windmill` table in ModelarDB after startup.                                                |
| output-plugin-builder | Utility service used to build the binary for the [Telegraf](https://www.influxdata.com/time-series-platform/telegraf) output plugin.                     |
| telegraf              | [Telegraf](https://www.influxdata.com/time-series-platform/telegraf) server used to ingest MQTT data into the ModelarDB edge node.                       |

## Configuration

TODO: Configure the MQTT broker or topics

TODO: Configure the table that is ingested into

TODO: Configure ModelarDB edge settings (link to documentation).

## Features

TODO: How to access manager, edge, and cloud.

TODO: How to ingest with MQTT streamer

TODO: How to ingest normally.

TODO: How to query.
