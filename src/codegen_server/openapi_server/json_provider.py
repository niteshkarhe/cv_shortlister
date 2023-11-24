from flask.json.provider import JSONProvider
import json
from openapi_server.encoder import JSONEncoder

class CustomJSONProvider(JSONEncoder):
#class CustomJSONProvider():
    include_nulls = False

    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=JSONEncoder)

    def loads(self, s: str | bytes, **kwargs):
        return json.loads(s, **kwargs)