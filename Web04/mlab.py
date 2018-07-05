import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds121311.mlab.com:21311/c4e18-cms_app

host = "ds121311.mlab.com"
port = 21311
db_name = "c4e18-cms_app"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())