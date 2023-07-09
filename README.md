# spring

# Requirements

If you don't have Docker already installed, follow these [instructions](https://www.docker.com/products/docker-desktop/).

# Usage

1. `docker pull tsightler/ring-mqtt`
2. Follow the Authentication section [here](<https://github.com/tsightler/ring-mqtt/wiki/Installation-(Docker)>), specifically the Acquire the Refresh Token section that has you run the following command `docker run -it --rm --mount type=bind,source=<absolute path to spring repository>,target=/data --entrypoint /app/ring-mqtt/init-ring-mqtt.js tsightler/ring-mqtt`
3. Create a copy of .example-env file and call it .env
4. Modify MQTT_TOPICS in the .env, filling in location ID and device ID. To get the location ID from the ring.com, login to ring.com and look at the address bar in the browser. It will look similar to https://account.ring.com/account/dashboard?l=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx with the location ID being after '?l='.
5. `docker-compose up`

# Development

1. Start `VS Code`
2. Open `spring`
3. Run the `Dev Containers: Open Folder in Container...` command from the Command Palette or Quick Actions Status Bar
4. Select the `Dockerfile.dev` file
5. Wait until the development container is running
6. Have fun developing!
