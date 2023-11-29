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
