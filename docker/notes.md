# Docker

## What is docker

Docker is a virtualization tool which enables running application on specific machine without any dependency to host. It achieves this goal by creating image containing application with necessary environment and running it as a standalone process.

### Container vs Virtual Machine

Why do we need docker since there were already Virtual Machines (VMs)?

Important to say is that Operating System (OS) consists of two layers: Kernel (talks to hardware) and application layer. VM virtualize entire system whereas Docker virtualize just application layer. The difference is colossal:


Docker advantages over VM:
  - **size**: docker images are much smaller measured in MG instead of GB
  - **speed**: docker containers starts much faster (no need to boot all system) and it is faster to create docker image then VM
  - **portability**: consistent behavior on different environments (dev, prod, test) where VM depends on host and its configuration
  - **replication**: both images and VM can be replicated but cost of VM replication might be big

Docker disadvantages:
  - **compatibility**: docker was created for Linux apps and may have problems with Windows apps whereas VM supports multiple OS and applications
  - **security**: if attacker breaks into container then entire machine might be down, if breaks VM then only VM is down.
  - **isolation**: docker image makes use of host kernel whereas VM is completely isolated


So, VM should be used when security and strong isolation is required like 'Airport flights managing systems'


### Development process before containers

Before containers developers had to prepare instruction how to setup environment on production. There are many points where something could go wrong, many possibilities of human errors and miscommunication. And moreover on host machine there was a problem when two application required two versions of the same library which were incompatible.

### Development process with containers

Developers develop their application. Create Dockerfile with instructions how to setup environment and copying application into image. Then build image.

Operations teams get this image. They run it and creates container. From Operation point of view much less points of failures, just run what they got.

## What is container and image?

Container is a running instance of image.
Image is an application with all necessary environment dependencies, tools, libraries and file system.

The inside of container looks like 'linux file system' with developed application

## Containers ports

Web applications transfer data using physical host ports. Since application is located inside container we must know which host port is used by application.

Container may be associated with more then one host port. Different containers can open ports with the same number but they must refer to different ports on host machine. We will get error if we would try to open one port for few applications

## Docker network

Local host network will connect to docker network. In docker network there might be multiple containers running which can communicate to each other.

## Docker compose

If we have application that is standalone and do not rely on other images, then we do not need docker compose. But in most cases it is not so.

Without docker compose we would have to manually insert commands into terminal which is quite problematic and error prone.

Instead of running commands individually we can create yaml file which will do it for us. To run/shutdown specific configuration do:
```
docker-compose -f <yaml_file> up
docker-compose -f <yaml_file> down
```
We do not need to specify network.

**NOTE**: docker compose is good for development of application (one node machine). On production it is better to use Kubernetes which handles master and slave nodes.

## Dockerfile

It is a file where there are recipes/commands how to create an image.

**FROM**  Use as a base image. Always start file with this.<p>
**ENV** VAR=value  set environment variable which will be accessible when running container<p>
**RUN** Execute shell command but it will have an effect in image <p>
**COPY** Execute copy command from host to image<p>
**CMD** Entry point when container starts. Only one possible

Note:
1) It is possible to have multiple FROM statements