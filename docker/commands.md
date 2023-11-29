## exec

Run interactive terminal in container
```
docker exec -it <container_id> /bin/bash
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

 -p <host_port>:<container_port>; bind ports. Note, host port has to be free

 -v <host_dir>:<container_dir>; map directory on host to container dir


## images

Print all images
```
docker images
```
