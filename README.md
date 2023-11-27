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
When configuring the pilot environment, the modified images need to be recreated and the services need to be restarted.

When the pilot is started, the [Telegraf](https://www.influxdata.com/time-series-platform/telegraf) server tries to 
connect to a local MQTT broker running at `tcp://127.0.0.1:1883`. To change this, change the `servers` setting in the
`[[inputs.mqtt_consumer]]` section of [telegraf.conf](telegraf/telegraf.conf). Below `servers` the topics that are 
subscribed to can be changed. Currently, the [Telegraf](https://www.influxdata.com/time-series-platform/telegraf) server
only subscribes to `/mqttstreamer/testtopic`.

The [Telegraf](https://www.influxdata.com/time-series-platform/telegraf) server ingests data into the 
`windmill` table that is created when the pilot is deployed. The table name can be configured by changing the `table` 
setting in [sample.conf](telegraf/sample.conf) and modifying the `CREATE MODEL TABLE` statement in [utility.py](utility.py). 
The schema of the created table can also be configured in [utility.py](utility.py). More information on the 
`CREATE MODEL TABLE` syntax is provided in the ModelarDB-RS 
[User](https://github.com/ModelarData/ModelarDB-RS/blob/main/docs/user/README.md#ingest-data) documentation. Note that 
if the schema of the table is changed, an equivalent change must be made to [telegraf.conf](telegraf/telegraf.conf).
Specifically, the columns of the table must match the columns specified under `[inputs.mqtt_consumer.xpath.fields]`.

Finally, it is also possible to configure the ModelarDB edge node to transfer data more or less frequently to the
[MinIO](https://min.io/) remote object store. This is done by adjusting the `MODELARDBD_UNCOMPRESSED_DATA_BUFFER_CAPACITY`,
`MODELARDBD_COMPRESSED_RESERVED_MEMORY_IN_BYTES`, and `MODELARDBD_TRANSFER_BATCH_SIZE_IN_BYTES` environment variables for
the service `modelardb-edge` in [docker-compose.yml](docker-compose.yml).

## Features

TODO: How to access manager, edge, and cloud.

TODO: How to ingest with MQTT streamer

TODO: How to ingest normally.

TODO: How to query.
