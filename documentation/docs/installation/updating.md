# How to update Hummingbot

## Update via Docker

We regularly update Hummingbot (see [Releases](/release-notes/)) and recommend users to regularly update their installations to get the latest version of the software.  

Updating to the latest docker image (e.g. `bitcoinsfacil/marketmaker_nmbi:latest`) requires users to (1) delete any instances of Hummingbot using that image, (2) delete the old image, and (3) recreate the Hummingbot instance:

```bash tab="Script"
wget https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/docker-commands/update.sh
chmod a+x update.sh
./update.sh
```

```bash tab="Detailed Commands"
# 1) Delete instance
docker rm hummingbot-instance

# 2) Delete old hummingbot image
docker image rm bitcoinsfacil/marketmaker_nmbi:latest

# 3) Re-create instance with latest hummingbot release
docker run -it \
--name hummingbot-instance \
--mount "type=bind,source=$(pwd)/navcoin_files/navcoin_conf,destination=/conf/" \
--mount "type=bind,source=$(pwd)/navcoin_files/navcoin_logs,destination=/logs/" \
bitcoinsfacil/marketmaker_nmbi:latest
```


## Update from source

Download the latest code from GitHub:

```
# From the hummingbot root folder:
git pull origin master

# Recompile the code:
conda deactivate
./uninstall
./clean
./install
conda activate hummingbot
./compile
bin/hummingbot.py
```

Alternatively, use our automated script:

```
# From the *root* folder:
wget https://raw.githubusercontent.com/bitcoinsfacil/marketmaker_nmbi/development/installation/install-from-source/update.sh
chmod a+x update.sh
./update.sh
```


## Installing from specific version via Docker
`$TAG` = Hummingbot version e.g. `version-0.16.0` For more information, visit the list of versions of [Hummingbot tags](https://hub.docker.com/r/bitcoinsfacil/marketmaker_nmbi/tags).

```
$ ./create.sh 

** ✏️  Creating a new Hummingbot instance **

ℹ️  Press [enter] for default values.

➡️  Enter Hummingbot version: [latest|development] (default = "latest")
$TAG
```
