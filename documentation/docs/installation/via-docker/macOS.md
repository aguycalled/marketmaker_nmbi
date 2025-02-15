# macOS Installation Using Docker

## Step 1. Install Docker

You can install Docker by [downloading an installer](https://docs.docker.com/v17.12/docker-for-mac/install/) from the official page. After you have downloaded and installed Docker, restart your system if necessary.

## Step 2. Install Hummingbot

You can install Hummingbot by selecting ***either*** of the following options from the tabs below:

1. **Easy Install**: download and use automated install scripts.
2. **Manual Installation**: run install commands manually.

```bash tab="Option 1: Easy Install"
# 1) Download Hummingbot install script
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/create.sh -o create.sh

# 2) Enable script permissions
chmod a+x create.sh

# 3) Run installation
./create.sh
```

```bash tab="Option 2: Manual Installation"
# 1) Create folder for your new instance
mkdir navcoin_files

# 2) Create folders for log and config files
mkdir navcoin_files/navcoin_conf && mkdir navcoin_files/navcoin_logs

# 3) Launch a new instance of hummingbot
docker run -it \
--name hummingbot-instance \
--mount "type=bind,source=$(pwd)/navcoin_files/navcoin_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/navcoin_files/navcoin_logs,destination=/logs/" \
bitcoinsfacil/marketmaker_nmbi:latest
```
