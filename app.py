import json
import hashlib

from flask import Flask, jsonify, request, Blueprint
from dateutil.parser import parse
from model import db, User

api = Blueprint('api', __name__)


@api.route('/users', methods=['POST'])
def create_users():
    users = request.json
    md5 = hashlib.md5()
    response = []

    for user in users:
        md5checksum = user.pop('md5checksum')
        md5.update(json.dumps(user))
        if md5checksum == md5.hexdigest():
            user['date'] = parse(user['date'])
            User(**user).save()
            response.append({'saved': 1})
        else:
            response.append({'saved': 0})

    return jsonify({'status': response})


@api.route('/users/search', methods=['GET'])
def search_users():
    user = User.objects(uid=request.args['uid'])
    response = {'count': user.count()}
    return jsonify(response)


def create_app(config={'MONGODB_SETTINGS': {'DB': "assignment"}}):
    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = config['MONGODB_SETTINGS']
    app.register_blueprint(api)
    db.init_app(app)
    return app
