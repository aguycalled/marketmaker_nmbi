# Running Hummingbot via Docker

Using a pre-compiled version of Hummingbot from Docker allows you to run instances with a few simple commands.

Docker images of Hummingbot are available on Docker Hub at [bitcoinsfacil/marketmaker_nmbi](https://hub.docker.com/r/bitcoinsfacil/marketmaker_nmbi).

## Automated Docker Scripts (Optional)

We have created helper scripts that simplify the process of installing and running Hummingbot with Docker:

* `create.sh`: Creates a new instance of Hummingbot
* `start.sh`: Starts Hummingbot
* `update.sh`: Updates Hummingbot

### What do the scripts do?

The scripts help you install an instance of Hummingbot and set up folders to house your logs and configuration files.

For more details, navigate to [Github: Hummingbot Docker scripts](https://github.com/bitcoinsfacil/marketmaker_nmbi/tree/development/installation/docker-commands).

mkdir /navcoin_conf && mkdir conf_files/navcoin_logs
navcoin_files       # Top level folder for hummingbot-related files
├── navcoin_conf    # Maps to hummingbot's conf/ folder, which stores configuration files
└── navcoin_logs    # Maps to hummingbot's logs/ folder, which stores log files

```
navcoin_files       # Top level folder for hummingbot-related files
├── navcoin_conf    # Maps to hummingbot's conf/ folder, which stores configuration files
└── navcoin_logs    # Maps to hummingbot's logs/ folder, which stores log files
```

!!! warning
    When you update Hummingbot, use the `update.sh` helper script. Do not delete these folders; otherwise, your configuration info may be lost.

### How do I use the scripts?

Copy the commands below and paste into Terminal to download and enable the automated scripts.

```bash tab="Linux"
wget https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/create.sh
wget https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/start.sh
wget https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/update.sh
chmod a+x *.sh
```

```bash tab="MacOS"
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/create.sh -o create.sh
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/start.sh -o start.sh
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/update.sh -o update.sh
chmod a+x *.sh
```

```bash tab="Windows (Docker Toolbox)"
cd ~
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/create.sh -o create.sh
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/start.sh -o start.sh
curl https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/update.sh -o update.sh
chmod a+x *.sh
```

## Basic Docker Commands for Hummingbot

#### Create Hummingbot Instance

The following commands will (1) create folders for config and log files, and (2) create and start a new instance of Hummingbot:

```bash tab="Detailed Commands"
# 1) Go root and create new user
sudo -i
adduser humming_nav
usermod -aG sudo humming_nav

# 2) update
sudo apt update

# 3) download docker repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

# 4) update and install docker
sudo apt update
sudo apt install docker-ce

# 5) add user to docker and check docker status
sudo usermod -aG docker humming_nav
systemctl status docker
# press Ctrl+C to get out of systemctl

# 6) enter user
su - humming_nav

# 7) clone hummingbot (username and password)
git clone https://github.com/bitcoinsfacil/marketmaker_nmbi.git marketmaker_nmbi
cd marketmaker_nmbi

# 8) build docker image (this can take a while)
docker build -t marketmaker_nmbi .

# 9) create config files
cd ~
mkdir conf_files
mkdir conf_files/navcoin_conf && mkdir conf_files/navcoin_logs

# 10)
docker run -it \
--name market-navcoin-container \
--mount "type=bind,source=$(pwd)/conf_files/navcoin_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/conf_files/navcoin_logs,destination=/logs/" \
marketmaker_nmbi
```


#### Restarting Hummingbot after Shutdown or Closing the Window

If you have previously created an instance of Hummingbot, the following command connects to the instance:

```bash tab="Script"
./start.sh
```

```bash tab="Detailed Commands"
# 1) Start hummingbot instance
docker start market-navcoin-container

# 2) Connect to hummingbot instance
docker attach market-navcoin-container
```

#### Running bot in background
##### Follow previous steps in ("Create Hummingbot Instance") if not made untill step 10
##### change instance `--name` parameter adding the number of instance at the end 
```bash tab="Detailed Commands"
# 10)
docker run -it \
--name market-navcoin-container_1 \
--mount "type=bind,source=$(pwd)/conf_files/navcoin_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/conf_files/navcoin_logs,destination=/logs/" \
marketmaker_nmbi
```

Press keys `ctrl+P` then `ctrl+Q` in sequence to detach from Docker (i.e. return to command line). This exits out of Hummingbot without shutting down the container instance.

#### Run several instances ()


## Hummingbot Setup

#### Docker Command Parameters

The instructions on this page assume the following default variable names and/or parameters.  You can customize these names.

Parameter | Description
---|---
`navcoin_files` | Name of the folder where your config and log files will be saved
`hummingbot-instance` | Name of your instance
`latest` | Image version, e.g. `latest`, `development`, or a specific version such as `0.9.1`
`navcoin_conf` | Folder in `navcoin_files` where config files will be saved (mapped to `conf/` folder used by Hummingbot)
`navcoin_logs` | Folder in `navcoin_files` where logs files will be saved (mapped to `logs/` folder used by Hummingbot)

#### Config and Log Files

The above methodology requires you to explicitly specify the paths where you want to mount the `conf/` and `logs/` folders on your local machine.

The example commands above assume that you create three folders:

```
navcoin_files       # Top level folder for hummingbot-related files
├── navcoin_conf    # Maps to hummingbot's conf/ folder, which stores configuration files
└── navcoin_logs    # Maps to hummingbot's logs/ folder, which stores log files
```

!!! info "`docker run` command and the `navcoin_files` folder"
    - The `docker run` command (when creating a new instance or updating Hummingbot version) must be run from the folder that contains the `navcoin_files` folder. By default, this should be the root folder.
    - You must create all folders prior to using the `docker run` command.

## Reference: Useful Docker Commands

Command | Description
---|---
`docker ps` | List all running containers
`docker ps -a` | List all created containers (including stopped containers)
`docker attach hummingbot-instance` | Connect to a running Docker container
`docker start hummingbot-instance` | Start a stopped container
`docker inspect hummingbot-instance` | View details of a Docker container, including details of mounted folders
