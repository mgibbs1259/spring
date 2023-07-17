# spring



# Requirements

If you don't have Docker already installed, follow these [instructions](https://www.docker.com/products/docker-desktop/).

# Usage

## Configuration

### Ring Devices
1. `docker pull tsightler/ring-mqtt`
2. Follow the Authentication section [here](<https://github.com/tsightler/ring-mqtt/wiki/Installation-(Docker)>), specifically the Acquire the Refresh Token section that has you run the following command `docker run -it --rm --mount type=bind,source=<absolute path to spring repository>,target=/data --entrypoint /app/ring-mqtt/init-ring-mqtt.js tsightler/ring-mqtt`
3. Create a copy of .example-env file and call it .env
4. You will need to modify MQTT_LOCATION_ID and MQTT_DEVICE_IDS in the .env, filling in location ID and device IDs. To get the location ID and device IDs, run `docker compose up` from within the spring directory. Then, inspect the console output and search for `Starting Device Discovery...`. For the location of interest, note the location ID (comes after `New location:` and is in `()`) in the .env file. Then for the devices of interest within the location of interest, note the device IDs (comes after `New device:` and is in `()`) in the .env file. Then, `Ctrl + C` and `docker compose down --rmi all`.

### Sprinkler Zones
1. Go to `https://app.rach.io/login` and login. Go to `Settings` > `Get API Key`. Then, add this to the .env file. 
2. Run `python configure_sprinklers.py` to obtain a dictionary containing 'zone name': 'zone ID'. Then, add the zone IDs of interest to the .env file. ***Note*** I believe you can only run one zone at a time. If you list multiple zone IDs, they will be run sequentially in the order that you listed them in the .env file. s

## Spring
1. Start spring by running `docker compose up -d`
2. Stop spring by running `docker compose down`

# Development
1. Start `VS Code`
2. Open `spring`
3. Run the `Dev Containers: Open Folder in Container...` command from the Command Palette or Quick Actions Status Bar
4. Select the `Dockerfile.dev` file
5. Wait until the development container is running
6. Have fun developing!
