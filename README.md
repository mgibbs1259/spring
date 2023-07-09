# spring

# Requirements

If you don't have Docker already installed, follow these [instructions](https://www.docker.com/products/docker-desktop/).

# Usage

1. `docker pull tsightler/ring-mqtt`
2. Follow the Authentication section [here](<https://github.com/tsightler/ring-mqtt/wiki/Installation-(Docker)>), specifically the Acquire the Refresh Token section that has you run the following command `docker run -it --rm --mount type=bind,source=<absolute path to spring repository>,target=/data --entrypoint /app/ring-mqtt/init-ring-mqtt.js tsightler/ring-mqtt`
3. Create a copy of .example-env file and call it .env
4. You will need to modify MQTT_LOCATION_ID and MQTT_DEVICE_IDS in the .env, filling in location ID and device IDs. To get the location ID and device IDs, run `docker compose up` from within the spring directory. Then, inspect the console output and search for `Starting Device Discovery...`. For the location of interest, note the location ID (comes after `New location:` and is in `()`) in the .env file. Then for the devices of interest within the location of interest, note the device IDs (comes after `New device:` and is in `()`) in the .env file. Then, `Ctrl + C` and `docker compose down --rmi all`.
5. Start spring using `docker compose up -d`

# Development

1. Start `VS Code`
2. Open `spring`
3. Run the `Dev Containers: Open Folder in Container...` command from the Command Palette or Quick Actions Status Bar
4. Select the `Dockerfile.dev` file
5. Wait until the development container is running
6. Have fun developing!
