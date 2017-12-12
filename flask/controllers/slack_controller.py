from config.bootstrap import r, DAILY_KARMA
from decorators.headers import valid_token
from utils.response_util import error_response, ok_response
from utils.redis_util import transfer, signup, both_member, is_member
from flask import g, request, Response

class slack_controller:

    @valid_token
    def karma_send(self):
        try:
            team_id = request.form['team_id']
            user_id_sender = request.form['user_id_sender']
            user_id_receiver = request.form['user_id_receiver']

            # Only for signed up user
            if both_member(r, team_id, user_id_sender, user_id_receiver):
                karma_user_id_sender = r.get(team_id+':'+user_id_sender+':karma:today')
                from_karma_given = r.hget(team_id+':'+user_id_sender, 'karma_given')
                target_karma_count = r.hget(team_id+':'+user_id_receiver, 'karma_count')

                if ((int(karma_user_id_sender) - 1) >= 0):
                    pipe = r.pipeline()
                    transfer(pipe, team_id, user_id_sender, from_karma_given, user_id_receiver, target_karma_count)

                    return ok_response({
                        'success' : True,
                        'sender' : {
                            'user_id' : user_id_sender,
                            'karma_left' : r.get(team_id+':'+user_id_sender+':karma:today')
                        },
                        'receiver' : {
                            'user_id' : user_id_receiver,
                            'karma_count' : r.hget(team_id+':'+user_id_receiver,'karma_count')
                        }
                    })
                else :
                    return ok_response({
                        'success' : False,
                        'error_code': 1,
                        'message':'Not enough karma'
                    })
            elif is_member(r, team_id, user_id_sender) == False :
                return ok_response({
                    'success' : False,
                    'error_code': 3,
                    'message':'Sender is not signedup.'
                })
            elif is_member(r, team_id, user_id_receiver) == False :
                return ok_response({
                    'success' : False,
                    'error_code': 4,
                    'message':'Receiver is not signedup.'
                })
        except Exception as e:
            return error_response()


    @valid_token
    def karma_remaining(self):
        try:
            team_id = request.form['team_id']
            user_id = request.form['user_id']

            if is_member(r, team_id, user_id):
                karma_points_remaining = r.get(team_id+':'+user_id+':karma:today')
                karma_points_count = r.hget(team_id+':'+user_id, 'karma_count')
                karma_points_given = r.hget(team_id+':'+user_id, 'karma_given')

                return ok_response({
                    'karma_points_count': karma_points_count,
                    'karma_points_given': karma_points_given,
                    'karma_points_remaining': karma_points_remaining
                })
            else :
                return ok_response({
                    'success' : False,
                    'error_code': 5,
                    'message':'Not Signed Up.'
                })
        except Exception as e:
            return error_response()


    @valid_token
    def leaderboard(self):
        try:
            team_id = request.form['team_id']

            leaderboard = r.zrevrange(team_id+':'+'leaderboard', 0, 10, 'withscores')
            top10 = []

            for lead in leaderboard:
                top10.append(lead)

            return ok_response(top10)
        except Exception as e:
            return error_response()

    @valid_token
    def signup(self):
        try:
            team_id = request.form['team_id']
            user_id = request.form['user_id']

            if r.sadd(team_id+':members', user_id):
                pipe = r.pipeline()
                signup(pipe, team_id, user_id, DAILY_KARMA)

                return ok_response({
                    'success': True
                })
            else :
                return ok_response({
                    'success': False,
                    'error_code': 2,
                    'message': 'Already signed up.'
                })
        except Exception as e:
            return error_response()
