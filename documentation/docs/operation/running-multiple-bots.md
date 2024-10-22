# Running Multiple Bots

## Multiple bots via Docker

Create multiple instances using `./create.sh` script or `docker run..` command (see [Create Hummingbot Instance](/cheatsheets/docker/#create-hummingbot-instance)).

### Running in the background (via Docker)

Press keys `Ctrl+P` then `Ctrl+Q` in sequence to detach from Docker (i.e. return to command line). This exits out of Hummingbot without shutting down the container instance.

Restart or connect to a running instance using `./start.sh` or `docker start.. && docker attach..` command (see [Restarting Hummingbot after Shutdown Closing the Window](/cheatsheets/docker/#restarting-hummingbot-after-shutdown-or-closing-the-window)).

For more information: [Docker Commands](/cheatsheets/docker/#reference-useful-docker-commands)


## Multiple bots from source

!!! tip
    We recommend that users download and install Hummingbot separately for each instance they wish to run.

Below command downloads the Hummingbot repository from GitHub where `$FOLDER_NAME` is the name of the separate directory.

```
cd ~
git clone https://github.com/bitcoinsfacil/marketmaker_nmbi.git $FOLDER_NAME
```

Do another install in the new directory.

```
cd $FOLDER_NAME
./install
conda activate hummingbot
./compile
```

### Running in the background (from source)

Use either `tmux` or `screen` to run multiple bots installed from source. Check out these external links how to use them.

* [Getting started with Tmux](https://linuxize.com/post/getting-started-with-tmux/)
* [How to use Linux Screen](https://linuxize.com/post/how-to-use-linux-screen/)

When using screen to run an instance in the background, run either of the following commands: `screen` or `screen -S $NAME`, where `$NAME` is what you wish to call this background instance. Use the latter to be more explicit if you want to run multiple bots.

Navigate to the folder where your separate Hummingbot is installed, then start the bot like normal.

```
conda activate hummingbot
bin/hummingbot.py
```

To exit the screen (detach), press `Ctrl+A` then `Ctrl+D` in sequence.

To list all running instances, use `screen -ls`.

![List Screen Instances](/assets/img/screen1.png)

Log back into the screen by using either `screen` or `screen -r $NAME` to open a specific instance.

<small>Credits to discord user `@matha` for this question and `@pfj` for the solution.</small>
