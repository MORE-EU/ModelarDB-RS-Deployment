from time import sleep

import pyarrow

from pyarrow import flight


def do_action(flight_client, action_type, action_body_str):
    action_body = str.encode(action_body_str)
    action = pyarrow.flight.Action(action_type, action_body)
    response = flight_client.do_action(action)

    print(list(response))


if __name__ == "__main__":
    edge_client = flight.FlightClient("grpc://host.docker.internal:9999")

    # Connect to the manager node and create the table that should be used for ingestion.
    manager_client = flight.FlightClient("grpc://host.docker.internal:9998")

    do_action(
        manager_client,
        "CommandStatementUpdate",
        "CREATE MODEL TABLE windmill(timestamp TIMESTAMP, temperature FIELD, wind_speed FIELD)",
    )

    # Compress all uncompressed data in the edge and flush it to the cloud once every 60 seconds.
    while True:
        sleep(60)
        do_action(edge_client, "FlushEdge", "")
