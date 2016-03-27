# Simple Flask application & deployment

This repository is a example of a simple Flask application:

- Flask application which implement several simple APIs.
- uWSGI & supervisor to run the flask application & manage the application process
- Ansible playbook to deploy MongoDB & the application
- Vagrantfile to provision the virtual machine for deployment

# Get Started

Download & install the following applications:

- VirtualBox (5.0.16 r105871)
- Vagrant (1.8.1)
- Ansible (2.0.1)
- Python (2.7)

For production run:
```
vagrant up
```

#### For development, run the application locally by:

```
# install mongodb
$ brew install mongodb

# set up virtual environment & install python dependency
$ virtualenv .virtualenv
$ source .virtualenv/bin/activate
(.virtualenv) $ pip install -r requirements.txt

# start the application in debug mode
(.virtualenv) $ python app.py
```

#### For testting:
```
(.virtualenv) $ nosetests
```