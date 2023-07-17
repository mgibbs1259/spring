import os
import logging
from dotenv import load_dotenv

import spring.control_ring as cr
import spring.control_sprinklers as cs


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if os.path.exists(".env"):
        load_dotenv(".env")

    client = cr.connect_to_mqtt_broker(
        os.environ["MQTT_CLIENT_ID"],
        os.environ["MQTT_USERNAME"],
        os.environ["MQTT_PASSWORD"],
        os.environ["MQTT_BROKER"],
        os.environ["MQTT_PORT"],
    )

    client = cr.subscribe_mqtt_broker_to_topic(
        client, os.environ["MQTT_LOCATION_ID"], os.environ["MQTT_DEVICE_IDS"]
    )

    sprinklers = cs.conenct_to_sprinklers(os.environ["RACHIO_API_KEY"])
    zone_ids = os.environ["RACHIO_ZONE_IDS"]
    run_seconds = int(os.environ["RACHIO_RUN_SECONDS"])

    client = cr.set_mqtt_broker_response_to_person_detected_message(
        client, lambda: cs.start_sprinklers(sprinklers, zone_ids, run_seconds)
    )

    client.loop_forever()
