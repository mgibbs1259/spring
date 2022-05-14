from pprint import pprint
from dotenv import load_dotenv

from ring_doorbell import Ring

import src.control_ring as cr


if __name__ == "__main__":
    load_dotenv()

    ring_auth = cr.perform_ring_auth()
    ring = Ring(ring_auth)
    ring.update_data()

    devices = ring.devices()
    pprint(devices)
