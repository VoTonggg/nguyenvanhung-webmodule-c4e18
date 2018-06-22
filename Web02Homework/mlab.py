import mongoengine

#mongodb://admin:admin1@ds161790.mlab.com:61790/muadongkhonglanh-c4e18


host = "ds161790.mlab.com"
port = 61790
db_name = "muadongkhonglanh-c4e18"
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