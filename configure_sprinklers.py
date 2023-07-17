import os
import logging
from dotenv import load_dotenv

import spring.control_sprinklers as cs


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if os.path.exists(".env"):
        load_dotenv(".env")

    sprinklers = cs.conenct_to_sprinklers(os.environ["RACHIO_API_KEY"])
    cs.list_sprinkler_information(sprinklers)
