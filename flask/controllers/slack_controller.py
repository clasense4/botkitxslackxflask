from config.bootstrap import r
from decorators.headers import valid_token
from utils.response_util import error_response, ok_response, transfer
from flask import g, request, Response

class slack_controller:

    @valid_token
    def karma_send(self):
        """
        Send karma if ok, send error if karma is not enough
        Need 3 params
        """
        try:
            team_id = request.form['team_id']
            user_id_from = request.form['user_id_from']
            user_id_target = request.form['user_id_target']

            karma_user_id_from = r.get(team_id+':'+user_id_from+':karma:today')

            from_karma_given = r.hget(team_id+':'+user_id_from, 'karma_given')
            target_karma_count = r.hget(team_id+':'+user_id_target, 'karma_count')

            if ((int(karma_user_id_from) - 1) >= 0):
                pipe = r.pipeline()
                transfer(pipe, team_id, user_id_from, from_karma_given, user_id_target, target_karma_count)
                return ok_response({
                    'from' : {
                        'user_id' : user_id_from,
                        'karma_left' : r.get(team_id+':'+user_id_from+':karma:today')
                    },
                    'target' : {
                        'user_id' : user_id_target,
                        'karma_count' : r.hget(team_id+':'+user_id_target,'karma_count')
                    }
                })
            else :
                return ok_response({'message':'Not enough karma'})
        except Exception as e:
            return error_response()


    @valid_token
    def karma_remaining(self):
        try:
            team_id = request.form['team_id']
            user_id = request.form['user_id']

            karma_points_remaining = r.get(team_id+':'+user_id+':karma:today')
            karma_points_count = r.hget(team_id+':'+user_id, 'karma_count')
            karma_points_given = r.hget(team_id+':'+user_id, 'karma_given')
            return ok_response({
                'karma_points_count': karma_points_count,
                'karma_points_given': karma_points_given,
                'karma_points_remaining': karma_points_remaining
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