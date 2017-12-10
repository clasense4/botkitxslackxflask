from flask import g, request, Response
from functools import wraps
from config.bootstrap import APP_KEY
import json

def valid_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.has_key('X-App-Key'):
            if (request.headers['X-App-Key'] != APP_KEY):
                msg = {"error": True, "message":"Token is missing or token is not correct."}
                resp = Response(response=json.dumps(msg),
                                status=400, \
                                mimetype="application/json")
                return resp
        else:
                msg = {"error": True, "message":"Header is not correct."}
                resp = Response(response=json.dumps(msg),
                                status=400, \
                                mimetype="application/json")
                return resp
        return f(*args, **kwargs)
    return decorated_function