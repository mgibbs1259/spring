# spring

<img src="https://github.com/mgibbs1259/spring/assets/32986518/68b3ea94-a14b-42c2-baaa-0dee070c3b43" width="600" height="100">

spring leverages the capabilities of Ring cameras and Rachio sprinklers to orchestrate a harmonious collaboration between surveillance and irrigation systems. To use spring, select the Ring cameras that monitor your desired property areas for human trespassers and their corresponding Rachio sprinkler zones. When the Ring cameras detect a person within the monitored areas, the Rachio sprinkler zones will activate for a predefined duration, ensuring a hilarious and memorable deterrent against unwanted visitors.

# Requirements

If you don't have Docker already installed, follow these [instructions](https://www.docker.com/products/docker-desktop/).

# Configuration

Create a copy of .example-env file and call it .env

## Ring Devices

1. `docker pull tsightler/ring-mqtt`
2. Follow the Authentication section [here](<https://github.com/tsightler/ring-mqtt/wiki/Installation-(Docker)>), specifically the Acquire the Refresh Token section that has you run the following command `docker run -it --rm --mount type=bind,source=<absolute path to spring repository>,target=/data --entrypoint /app/ring-mqtt/init-ring-mqtt.js tsightler/ring-mqtt`
3. You will need to modify MQTT_LOCATION_ID and MQTT_DEVICE_IDS in the .env, filling in location ID and device IDs. To get the location ID and device IDs, run `docker compose up` from within the spring directory. Then, inspect the console output and search for `Starting Device Discovery...`. For the location of interest, note the location ID (comes after `New location:` and is in `()`) in the .env file. Then for the devices of interest within the location of interest, note the device IDs (comes after `New device:` and is in `()`) in the .env file. Then, `Ctrl + C` and `docker compose down --rmi all`.

## Rachio Sprinklers

1. You will need to modify RACHIO_API_KEY in the .env, filling in the Rachio API key. Go to `https://app.rach.io/login` and login. Go to `Settings` > `Get API Key`. Then, add the Rachio API key to the .env file.
2. You will need to modify RACHIO_ZONE_IDS in the .env, filling in the sprinkler zone IDs. Run `python configure_sprinklers.py` to see a dictionary containing 'zone name': 'zone ID' in the console output. Then, add the zone IDs of interest to the .env file. **_Note:_** I believe that you can only run one sprinkler zone at a time. If you list multiple zone IDs, they will run sequentially in the order that you listed them in the .env file.

# Usage

1. Start spring by running `docker compose up -d`
2. Stop spring by running `docker compose down`

# Development

1. Start `VS Code`
2. Open `spring`
3. Run the `Dev Containers: Open Folder in Container...` command from the Command Palette or Quick Actions Status Bar
4. Select the `Dockerfile.dev` file
5. Wait until the development container is running
6. Have fun developing!

# Thank You

-    tsightler - for [ring-mqtt](https://github.com/tsightler/ring-mqtt)
-    rfverbruggen - for [rachiopy](https://github.com/rfverbruggen/rachiopy)
-    Last but not least, my neighbors who inspired me to pursue this project
