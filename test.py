import json
import datetime
from flask.ext.testing import TestCase

from faker import Factory
from flask import url_for
from model import User
from app import create_app
from dateutil.parser import parse

fake = Factory.create()


class UserApiTestCase(TestCase):

    def create_app(self):
        flask_app = create_app({
            "MONGODB_SETTINGS":
                {'DB': "assignment_test"}
        })
        flask_app.config["TESTING"] = True
        return flask_app

    def tearDown(self):
        User.objects.delete({})

    def test_create_user(self):
        response = self.client.post(
            url_for('api.create_users'),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps([
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
            )
        )
        results = response.json['status']

        # Verify the results are returned correctly
        self.assertEqual(results[0]['saved'], 1)
        self.assertEqual(results[1]['saved'], 0)

        # Verify if the database is updated
        users = User.objects(uid=1)
        self.assertEqual(len(users), 1)
        user = users[0]
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.date, parse("2015-05-12T14:36:00.451"))

    def test_get_user(self):

        # When there is no user, no count
        response = self.client.get(url_for('api.search_users') + '?uid=4')
        self.assert200(response)
        self.assertEqual(0, response.json['count'])

        name = fake.name()
        User(uid=4, name=name, date=datetime.datetime.now()).save()
        response = self.client.get(url_for('api.search_users') + '?uid=4')
        self.assert200(response)
        self.assertEqual(1, response.json['count'])

        # Save more data & expect to have the count increases
        User(uid=4, name=name, date=datetime.datetime.now()).save()
        User(uid=4, name=name, date=datetime.datetime.now()).save()
        User(uid=4, name=name, date=datetime.datetime.now()).save()
        User(uid=4, name=name, date=datetime.datetime.now()).save()
        response = self.client.get(url_for('api.search_users') + '?uid=4')
        self.assert200(response)
        self.assertEqual(5, response.json['count'])
