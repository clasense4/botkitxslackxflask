from flask import Response
import json

def error_response(message='Bad Request', status=400):
    msg = {"error": True, "message": message}
    resp = Response(response=json.dumps(msg),
                    status=status, \
                    mimetype="application/json")
    return resp

def ok_response(message='OK', status=200):
    msg = {"data": message}
    resp = Response(response=json.dumps(msg),
                    status=status, \
                    mimetype="application/json")
    return resp
