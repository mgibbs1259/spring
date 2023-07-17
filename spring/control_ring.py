import os
import json
import logging
from datetime import datetime, timedelta
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
    client: mqtt_client.Client, location_id: str, device_ids: List[str]
) -> mqtt_client.Client:
    """Subscribes the MQTT client to the specified topics

    Args:
        client (mqtt_client.Client): The connected MQTT client
        location_id (str): The location ID
        device_ids (List[str]): The list of device IDs

    Returns:
        mqtt_client.Client: The subscribed MQTT client

    Raises:
        ValueError: If the client or topics parameter is missing
        Exception: If failed to subscribe to MQTT topics
    """
    if client is None:
        raise ValueError("Client parameter cannot be None")

    topics = []
    for i, device_id in enumerate(device_ids.split(",")):
        topics.append((f"ring/{location_id}/camera/{device_id}/motion/attributes", i))

    if not topics:
        raise ValueError("Topics parameter cannot be empty")

    try:
        client.subscribe(topics)
        logging.info("Successfully subscribed to MQTT topics")
    except Exception as e:
        raise Exception(f"Failed to subscribe to MQTT topics: {e}")

    return client


def set_mqtt_broker_response_to_person_detected_message(
    client: mqtt_client.Client,
    response: Optional[Callable[[str], None]] = None,
) -> mqtt_client.Client:
    """Sets up the MQTT client to handle incoming person detected messages

    Args:
        client (mqtt_client.Client): The connected MQTT client
        response (Optional[Callable[[str], None]]): Optional callback function to
        handle incoming person detected messages

    Returns:
        mqtt_client.Client: The configured MQTT client
    """

    def on_message(client, userdata, message):
        message_info = message.payload.decode()
        message_info = json.loads(message_info)
        logging.info(f"Received {message_info} from {message.topic} topic")

        person_detected = message_info["personDetected"]
        current_last_motion_time = os.environ.get("RING_LAST_MOTION")
        new_last_motion_time = message_info["lastMotionTime"]

        current_time = datetime.now()
        new_last_motion_time_dt = datetime.fromisoformat(new_last_motion_time[:-1])
        time_difference = current_time - new_last_motion_time_dt

        # Only run if person detected and prevent sprinklers from running multiple times for the same message
        if person_detected and time_difference <= timedelta(seconds=30):
            if current_last_motion_time != new_last_motion_time:
                os.environ["RING_LAST_MOTION"] = new_last_motion_time
                logging.info(
                    f"Environment variable RING_LAST_MOTION={current_last_motion_time} set to {new_last_motion_time}"
                )
                response()

    client.on_message = on_message

    return client
