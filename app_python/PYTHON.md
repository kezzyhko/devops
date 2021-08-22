# Information about the python app

This README contains the best practices I found about python.



## Frameworks

The task description tells to use "prod ready frameworks". I am familiar with two frameworks: *Django* and *Flask*. *Django* is usually used for more complex apps, and *Flask* is for more simple ones.

However, in my opinion, the current app requirements is too simple even for *Flask*, so I decided to use bare `http.server` python library without any frameworks.



## `if __name__ == '__main__':`

Even if you do not expect your file to be imported, it is still a good practice to use this check. At the very least, this convention helps with readability. Most python developers, if there is no such line in the code, will assume that the file is not supposed to be executed diffectly.



## Code style

As with all programming languages, it is important to select and follow one uniform codestyle throughout the whole project. Linters can help with that.
