# DevOps



## What is in this repo?

This is repository for the DevOps Engineering course in Innopolis University

* [`app_python`](app_python) folder contains python web app and necessary files for Docker.
* [`app_python/app_files`](app_python/app_files) folder contains the app itself, which shows current time in `Europe/Moscow` timezone. This app uses *Django* framework.



## Quick start

The simplest way is to use docker:  
`docker run -p 5000:5000 kezzyhko/devops`

If you do not want to use docker for some reason, then clone the repo, install `requirements.txt` and run `main.py`:  
`git clone https://github.com/kezzyhko/devops.git`  
`pip3 install -r ./devops/app_python/requirements.txt`  
`python3 ./devops/app_python/app_files/main.py`  

By default, app is accessible on port `5000`
