# Information about the Docker

The docker container for this app is accessible as [`kezzyhko/devops`](https://hub.docker.com/repository/docker/kezzyhko/devops)

This README contains the best practices I found about docker.



## 1. Use appropriate image

One of the common mistakes is to use general OS image (like `ubuntu:20.04`) and manually install anything you need using `apt`. There is no need from scratch, instead we can use `python` images.

Additionally, I used `alpine` image to reduce the side of the container



## 2. Copy only necessary files

The `Dockerfile` contains the following line: `COPY . /app`. Normally, it would copy all of the contents of current folder to the image. However, I used `.dockerignore`, so that extra files like cache, READMEs and other unnecessary files will not end up in the container



## 3. Dockerfile instructions order

Very frequently, people put `COPY` instruction immediatly after `FROM`. However, that prevents docker from using cached images with allready prepared environment. If app files change, docker will copy them, and then reinstall the whole `requirements.txt`. Since `requirements.txt` can not change without changing the source code of the app, there is no opposite problem.

So, in my `Dockerfile`, the line with `COPY` instruction is almost the last one, and it comes after preparing the environment.



## Other

Also, I found an official guide on best practices from Docker with more technical advides:  
<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/>
