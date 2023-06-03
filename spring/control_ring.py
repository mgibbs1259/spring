from typing import Callable, Optional

import paho.mqtt.client as mqtt_client


def connect_to_mqtt_broker(
    client_id: str, username: str, password: str, broker: str, port: int
) -> mqtt_client.Client:
    if not all((client_id, username, password, broker, port)):
        raise ValueError("All parameters must be provided")

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    try:
        client.connect(broker, int(port))
        print("Successfully connected to MQTT broker")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to MQTT broker: {e}")

    return client


def subscribe_mqtt_broker_to_topic(
    client: mqtt_client.Client, topics: str
) -> mqtt_client.Client:
    if client is None:
        raise ValueError("Client parameter cannot be None")

    if not topics:
        raise ValueError("Topics parameter cannot be empty")

    try:
        topics = topics.split(",")
        subscribe_topics = []
        for i, t in enumerate(topics):
            subscribe_topics.append((f"camera{i}", 0))
        client.subscribe(subscribe_topics)
        print("Successfully subscribed to MQTT topics")
    except Exception as e:
        raise Exception(f"Failed to subscribe to MQTT topics: {e}")

    return client


def set_mqtt_broker_response_to_message(
    client: mqtt_client.Client,
    response: Optional[Callable[[str], None]] = None,
) -> mqtt_client.Client:
    def on_message(client, userdata, message):
        message_info = message.payload.decode()
        print(f"Received {message_info} from {message.topic} topic")

        if response is not None:
            response(message_info)

    client.on_message = on_message

    return client
