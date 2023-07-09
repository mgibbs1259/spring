import logging
from typing import Callable, List, Optional

import paho.mqtt.client as mqtt_client


def connect_to_mqtt_broker(
    client_id: str, username: str, password: str, broker: str, port: int
) -> mqtt_client.Client:
    """Connects to an MQTT broker

    Args:
        client_id (str): The client ID for connecting to the broker
        username (str): The username for authentication
        password (str): The password for authentication
        broker (str): The hostname or IP address of the MQTT broker
        port (int): The port number of the MQTT broker

    Returns:
        mqtt_client.Client: The connected MQTT client

    Raises:
        ValueError: If any of the parameters are missing
        ConnectionError: If failed to connect to the MQTT broker
    """
    if not all((client_id, username, password, broker, port)):
        raise ValueError("All parameters must be provided")

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    try:
        client.connect(broker, int(port))
        logging.info("Successfully connected to MQTT broker")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to MQTT broker: {e}")

    return client


def subscribe_mqtt_broker_to_topic(
    client: mqtt_client.Client, topics: str
) -> mqtt_client.Client:
    """Subscribes the MQTT client to the specified topics

    Args:
        client (mqtt_client.Client): The connected MQTT client
        topics (str): The topics to subscribe to

    Returns:
        mqtt_client.Client: The subscribed MQTT client

    Raises:
        ValueError: If the client or topics parameter is missing
        Exception: If failed to subscribe to MQTT topics
    """
    if client is None:
        raise ValueError("Client parameter cannot be None")

    if not topics:
        raise ValueError("Topics parameter cannot be empty")

    try:
        client.subscribe(topics)
        logging.info("Successfully subscribed to MQTT topics")
    except Exception as e:
        raise Exception(f"Failed to subscribe to MQTT topics: {e}")

    return client


def set_mqtt_broker_response_to_message(
    client: mqtt_client.Client,
    response: Optional[Callable[[str], None]] = None,
) -> mqtt_client.Client:
    """Sets up the MQTT client to handle incoming messages

    Args:
        client (mqtt_client.Client): The connected MQTT client
        response (Optional[Callable[[str], None]]): Optional callback function to handle incoming messages

    Returns:
        mqtt_client.Client: The configured MQTT client
    """

    def on_message(client, userdata, message):
        message_info = message.payload.decode()
        logging.info(f"Received {message_info} from {message.topic} topic")

        if response is not None:
            response(message_info)

    client.on_message = on_message

    return client
