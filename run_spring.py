import os
import logging
from dotenv import load_dotenv

import spring.control_ring as cr


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if os.path.exists(".env-prod"):
        load_dotenv(".env-prod")

    client = cr.connect_to_mqtt_broker(
        os.environ["MQTT_CLIENT_ID"],
        os.environ["MQTT_USERNAME"],
        os.environ["MQTT_PASSWORD"],
        os.environ["MQTT_BROKER"],
        os.environ["MQTT_PORT"],
    )

    client = cr.subscribe_mqtt_broker_to_topic(client, os.environ["MQTT_TOPICS"])

    client = cr.set_mqtt_broker_response_to_message(client)

    client.loop_forever()
