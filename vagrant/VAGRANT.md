# Vagrant

The task says to use terrafom, but I had some problems using it. Instead, I decided to use vagrant.  
I selected Google Cloud as the cloud platform I will use. For this, I used [vagrant-google](https://github.com/mitchellh/vagrant-google) plugin.  

Here are some best practices I found about Vagrant:
* Control CPU and Memory
* Configure SSH securly, with 
* It should be Idempotent. Which means, that running multiple times should result in the same environment.
There were other more technical best practices, but they were not really applicable to my case, so I decided not to write them here.  
