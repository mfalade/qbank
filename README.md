# Q-Bank


#### Getting started
This project uses Python 3.6.1 and Django 1.11.3

#### Running Locally
Make sure you have docker and docker-compose installed on your machine


+ Clone the project 

    ```bash
    $ git clone https://github.com/mfalade/qbank
    ```
+ **cd** into the project directory and run
    ```bash
    $ docker-compose up
    ```
    This would start up a container and spin up a server on port **8000** 

+ In the console, you should see a message that says `You have <x> unapplied migrations ...

+ We need to apply our migrations first so the needed database tables get created. To do this, SSH into the container hosting the web app by running

    ```
    $ docker exec -t -i $(docker ps | grep 'qbank_web' | awk '{print $1}') bash
    ```
+ Once inside the container, at the prompt, run:
```
$ python3 manage.py migrate
```
+ This would apply the necessary migrations and you should be good to go.
+ Verify that everything is working as expected by visiting [http://localhost:8000](http://localhost:8000)



