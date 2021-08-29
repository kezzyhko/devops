# Information about the python app

This README contains the best practices I found about python.



## Frameworks

The task description tells to use "prod ready frameworks". I am familiar with two frameworks: *Django* and *Flask*. *Django*. This project uses *Django*.



## Python best practices


### `if __name__ == '__main__':`

Even if you do not expect your file to be imported, it is still a good practice to use this check. At the very least, this convention helps with readability. Most python developers, if there is no such line in the code, will assume that the file is not supposed to be executed diffectly.


### Code style

As with all programming languages, it is important to select and follow one uniform codestyle throughout the whole project. Linters can help with that.



## Unit Tests

The unit tests for this app are located at [`app_files/tests.py`](app_files/tests.py).  
There are three tests, which test the `datetime_view` view, located in the [`app_files/views.py`](app_files/views.py).

Here are some best practices I found about unit test:
* Tests should focus *small bits* of code
* Unit tests should be able to run independent of each other
* Since function names are written when test fails, their names should be descriptive, and might be long