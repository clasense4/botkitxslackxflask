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

def transfer(pipe, team_id, user_id_from, from_karma_given, user_id_target, target_karma_count):
    # pipe.multi()
    pipe.decr(team_id+':'+user_id_from+':karma:today')
    target_new_karma = int(target_karma_count) + 1
    pipe.hset(team_id+':'+user_id_target, 'karma_count', target_new_karma)
    from_new_karma = int(from_karma_given) + 1
    pipe.hset(team_id+':'+user_id_from, 'karma_given', from_new_karma)
    pipe.zadd(team_id+':'+'leaderboard', target_new_karma, user_id_target)
    pipe.execute()