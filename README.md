# docker-transmission-magnet-watch

## Subject

Observe Transmission's watch folder for magnet files and add them to Transmission automatically

## Description

Since Transmission is not supporting watching of the watch directory for magnet files, this docker container is adding that functionality.

## Supported Architectures

Simply pulling `marqusm/transmission-magnet-watch` should retrieve the correct image for your arch, but you can also pull specific arch images via tags.

The architectures supported by this image are:

| Architecture | Tag |
| :----: | --- |
| x86-64 | amd64-latest |
| arm64 | arm64v8-latest |
| armhf | arm32v7-latest |

## Usage

### Docker

```
docker run \
    -e TRANSMISSION_API="http://transmission:9091/transmission/rpc" \
    -v ~/transmission/data/watch:/watch \
    -v ~/transmission/data/completed:/completed \
    -v ~/transmission-magnet-watch/data:/data \
    transmission-magnet-watch
```

### Docker compose

```
version: "3"
services:
    transmission-magnet-watch:
        image: transmission-magnet-watch
        container_name: transmission-magnet-watch
        restart: unless-stopped
        environment:
          - TRANSMISSION_API=http://transmission:9091/transmission/rpc
        volumes:
          - ~/transmission/data/watch:/watch
          - ~/transmission/data/completed:/completed
          - ~/transmission-magnet-watch/data:/data
```

## Parameters

| Parameter | Function |
| :----: | --- |
| `TRANSMISSION_API` | Transmission's rpc api url |

## Versions

* **18.04.20:** - Initial Release.

## To Do

- Support Transmission's username/password