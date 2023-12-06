# Docker

## build

Build an image with:
```
docker build -t my-app:1.0 .
```
Options:

  - t - tag of an application
  - last argument is a location of a Dockerfile


## exec

Run interactive terminal in container
```
docker exec -it <container_id> /bin/bash
```

## docker network

Lists networks
```
docker network ls
```

Create network
```
docker network create <name>
```


## ps

Prints running containers
```
docker ps
```

Options:

  -a; print all containers even stopped


## pull

Pulls the image from repository (by default from docker hub)
```
docker pull <image>:<tag>
```

## rm

Removes containers

Remove stopped container:
```
docker rm $(docker ps -a -f status=exited -f status=created -q)
```


## run

Runs downloaded image. If
```
docker run <image>:<tag>
docker run -e POSTGRES_PASSWORD=password postgres:9.6
docker run -it <image> /bin/bash
```
Options:

 -d; run image in detached mode (release terminal)

 -e VAR=value; set specific env variable when starting

 --network <name>; run container in specific network

 -p <host_port>:<container_port>; bind ports. Note, host port has to be free

 -v <host_dir>:<container_dir>; map directory on host to container dir


## images

Print all images
```
docker images
```

# Docker compose

To run specific composition:
```
docker-compose -f <compose.yaml> up
docker-compose -f <compose.yaml> down
```