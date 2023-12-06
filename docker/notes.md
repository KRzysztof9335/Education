# Docker

## What is docker

Docker is a virtualization tool it enables running app on specific machine without any dependency to host.

### Container vs Virtual Machine

The Operating System consists of two layers: Kernel (talks to hardware) and application layer.

VM virtualize entire system whereas Docker virtualize just application layer. The difference is colossal:

  - docker images are much smaller MG instead of GB
  - docker containers starts much faster
  - if attacker break container then entire machine might be down, if breaks VM then only VM is down.


### Development process before containers

Before containers developers had to prepare instruction how to setup environment on production. There are many points where something could go wrong.

### Development process with containers

Developers develop their application and pack it into image, so operations teams just need to run image creating container

## What is container and image?

Container is a running instance of image.
Image is an application with all necessary environment dependencies and file system.

In container there is own virtual file system.

## Containers ports

Different containers can open ports with the same number but they must refer to different ports on host machine.

We will get error if we would try to open one port for few applications

## Docker network

Local host network will connect to docker network. In docker network there might be multiple containers running which can communicate to each other.

## Docker compose

Instead of running commands individually we can create yaml file which will do it for us. To run/shutdown specific configuration do:
```
docker-compose -f <yaml_file> up
docker-compose -f <yaml_file> down
```
We do not need to specify network.


## Dockerfile

It is a basic file to create images

FROM - Use as a base image. Always start file with this.
ENV VAR=value - set environment variable which will be accessible when running container
RUN Execute shell command but it will have an effect in image
COPY Execute copy command from host to image
CMD Entry point when container starts. Only one possible

Note:
1) It is possible to have multiple FROM statements