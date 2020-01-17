# Docker Instructions

Compiled versions of `hummingbot` are available on Docker Hub at [`bitcoinsfacil/marketmaker_nmbi`](https://hub.docker.com/r/bitcoinsfacil/marketmaker_nmbi).

## Running `hummingbot` with Docker

For instructions on operating `hummingbot` with Docker, navigate to [`hummingbot` documentation: Install with Docker](https://docs.hummingbot.io/installation/docker/).

---

## Development commands: deploying to Docker Hub

### Create docker image

```sh
# Build docker image
$ docker build -t bitcoinsfacil/marketmaker_nmbi:$TAG -f Dockerfile .

# Push docker image to docker hub
$ docker push bitcoinsfacil/marketmaker_nmbi:$TAG
```

#### Build and Push

```sh
$ docker image rm bitcoinsfacil/marketmaker_nmbi:$TAG && \
  docker build -t bitcoinsfacil/marketmaker_nmbi:$TAG -f Dockerfile \
  docker push bitcoinsfacil/marketmaker_nmbi:$TAG
```
