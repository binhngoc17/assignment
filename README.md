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

# API Docs

```
# Create entry in user table
POST /users
-d [
  {
    "uid": "1",
    "name": "John Doe",
    "date": "2015-05-12T14:36:00.451765",
    "md5checksum": "e8c83e232b64ce94fdd0e4539ad0d44f"
  },
  {
    "uid": "2",
    "name": "Jane Doe",
    "date": "2015-05-13T14:36:00.451765",
    "md5checksum": "b419795d50db2a35e94c8364978d898f"
  }
]

# response
{
    "results": [
        {"saved": 1},
        {"saved": 0}
    ]
}

# Count the number of entries in user table through filters: uid
GET /users/search?uid=<uid>

# response
{"count": 1}

```