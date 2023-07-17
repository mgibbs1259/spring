from rachiopy import Rachio


def conenct_to_sprinklers(rachio_api_key: str) -> Rachio:
    """Connects to the Rachio API and returns an instance of the Rachio object

    Args:
        rachio_api_key (str): The API key for accessing the Rachio API

    Returns:
        Rachio: An instance of the Rachio object connected to the API
    """
    sprinklers = Rachio(rachio_api_key)
    return sprinklers


def list_sprinkler_information(sprinklers: Rachio) -> None:
    """Lists the information of the connected sprinkler zones

    Args:
        sprinklers (Rachio): An instance of the Rachio object connected to the API

    Returns:
        None
    """
    resp, content = sprinklers.person.info()
    content_id = content["id"]
    zone_ids = {}
    for devices in sprinklers.person.get(content_id)[1]["devices"]:
        for zone in devices["zones"]:
            zone_ids[zone["name"]] = zone["id"]
    print(zone_ids)


def start_sprinklers(sprinklers: Rachio, zone_ids: str, seconds: int) -> None:
    """Starts the sprinklers for the specified zones for a given number of seconds

    Args:
        sprinklers (Rachio): An instance of the Rachio object connected to the API
        zone_ids (str): The sprinkler zone IDs
        seconds (int): The duration in seconds for which to run the sprinklers

    Returns:
        None
    """
    zones = []
    for i, zone_id in enumerate(zone_ids.split(",")):
        zones.append({"id": zone_id, "duration": seconds, "sortOrder": i})
    sprinklers.zone.start_multiple(zones)
