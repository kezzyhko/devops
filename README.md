[![Django CI](https://github.com/kezzyhko/devops/actions/workflows/django.yml/badge.svg)](https://github.com/kezzyhko/devops/actions/workflows/django.yml)
[![CI to Docker Hub](https://github.com/kezzyhko/devops/actions/workflows/dockerhub.yml/badge.svg)](https://github.com/kezzyhko/devops/actions/workflows/dockerhub.yml)


# DevOps

This is repository for the DevOps Engineering course in Innopolis University

Table of contents:  
[What is in this repo?](#what-is-in-this-repo)  
[Quick start](#quick-start)  
[Unit Tests](#unit-tests) 



## What is in this repo?

* [`app_python`](app_python) folder contains python web app and necessary files for Docker.
* [`app_python/app_files`](app_python/app_files) folder contains the app itself, which shows current time in `Europe/Moscow` timezone. This app uses *Django* framework.
* [`.github/workflows`](.github/workflows) folder contains workflows for testing the app and publishing it to the docker hub



## Quick start

The simplest way is to use docker:  
`docker run -p 5000:5000 kezzyhko/devops`

If you do not want to use docker for some reason, then clone the repo, install `requirements.txt` and run `main.py`:  
`git clone https://github.com/kezzyhko/devops.git`  
`pip3 install -r ./devops/app_python/requirements.txt`  
`python3 ./devops/app_python/app_files/main.py`  

By default, app is accessible on port `5000`



## Unit tests

The unit tests for this app are located at [`app_files/tests.py`](app_files/tests.py).  
There are three tests, which test the `datetime_view` view, located in the [`app_files/views.py`](app_files/views.py).
