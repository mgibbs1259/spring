from rachiopy import Rachio


def conenct_to_sprinklers(rachio_api_key: str) -> Rachio:
    sprinklers = Rachio(rachio_api_key)
    return sprinklers


def list_sprinkler_information(sprinklers: Rachio) -> None:
    resp, content = sprinklers.person.info()
    content_id = content["id"]
    zone_ids = {}
    for devices in sprinklers.person.get(content_id)[1]["devices"]:
        for zone in devices["zones"]:
            zone_ids[zone["name"]] = zone["id"]
    print(zone_ids)


def start_sprinklers(sprinklers: Rachio, zone_id: str, seconds: int) -> None:
    sprinklers.start(zone_id, seconds)
