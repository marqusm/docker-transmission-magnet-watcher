# docker-transmission-magnet-watcher

## Subject
Watching Transmission's watch folder for magnet files and add them to Transmission automatically

## Description
Since Transmission is not supporting watching of the watch directory for magnet files, this docker container is adding that functionality.

## Usage

### Docker
```
docker run \
    -e TRANSMISSION_API="http://transmission:9091/transmission/rpc" \
    -v ./transmission/data/watch:/watch \
    transmission-magnet-watcher
```

### Docker compose
```
version: "3"
services:
    transmission-magnet-watcher:
        image: transmission-magnet-watcher
        container_name: transmission-magnet-watcher
        restart: unless-stopped
        environment:
          - TRANSMISSION_API=http://transmission:9091/transmission/rpc
        volumes:
          - transmission/data/watch:/watch
```

## Parameters
| Parameter | Function |
| :----: | --- |
| `TRANSMISSION_API` | Transmission's rpc api url |


## Versions
* **1.0.0-alpha** - Initial Release.

## To Do
- Support Transmission's username/password
- Not running docker process as root
- Introduce PUID, PGID and TZ environment variables
- 