# Docker collection

This collection contains 2 roles and 1 playbook:  
* `installdocker` role just installs docker-ce
* `deploydockerimage` role creates container with given `image` variable, and forwards given `ports` variable
* `playbook.yml` is an example of using these roles. It uses both roles to deploy `kezzyhko/devops` docker image and forward port `5000`
