import ssl
from mongoengine import connect, Document, StringField, BooleanField, DateTimeField
from mongoengine.connection import get_connection, get_db
from marshmallow import Schema, fields, pprint
import datetime as dt
import pymongo


# Paste the following examples here
def connect_to_db():
    connection_string = "mongodb://melissa:rPVrVSU4dOlBGhXX@cluster0-97f1f.mongodb.net/?ssl=true"
    database_name = "todos"
    # "mongodb://user123:p455w0rd@gettingstarted-shard-00-00-hyjsm.mongodb.net:27017,gettingstarted-shard-00-01-hyjsm.mongodb.net:27017,gettingstarted-shard-00-02-hyjsm.mongodb.net:27017/test?ssl=true&replicaSet=GettingStarted-shard-0&authSource=admin"
    # client = MongoClient(connection_string, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
    # db = client.test
    connect(database_name)
    conn = get_connection()
    if isinstance(conn, pymongo.mongo_client.MongoClient):
        print("Connected to Mongo")
    else:
        return False
    db = get_db()
    if isinstance(db, pymongo.database.Database):
        print("Got a DB")
    else:
        return False
    if(db.name == database_name):
        print("connected to Test Db")
    else:
        return False


class TodoItem(Document):
    task = StringField(max_length=120, required=True)
    completed = BooleanField(default=False)
    created = DateTimeField(default=dt.datetime.now())


class TodoItemSchema(Schema):
    id = fields.Str()
    task = fields.Str()
    completed = fields.Bool()
    created = fields.DateTime()


connect_to_db()
