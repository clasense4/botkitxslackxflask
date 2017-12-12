def transfer(pipe, team_id, user_id_sender, from_karma_given, user_id_receiver, target_karma_count):
    # pipe.multi()
    pipe.decr(team_id+':'+user_id_sender+':karma:today')
    receiver_new_karma = int(target_karma_count) + 1
    pipe.hset(team_id+':'+user_id_receiver, 'karma_count', receiver_new_karma)
    sender_new_karma = int(from_karma_given) + 1
    pipe.hset(team_id+':'+user_id_sender, 'karma_given', sender_new_karma)
    pipe.zadd(team_id+':'+'leaderboard', receiver_new_karma, user_id_receiver)
    pipe.execute()

def signup(pipe, team_id, user_id, daily_karma):
    pipe.set(team_id+':'+user_id+':karma:today', daily_karma)
    pipe.hset(team_id+':'+user_id, 'karma_count', 0)
    pipe.hset(team_id+':'+user_id, 'karma_given', 0)
    pipe.zadd(team_id+':'+'leaderboard', 0, user_id)
    pipe.execute()

def is_member(r, team_id, user_id):
    return r.sismember(team_id+':members', user_id)

def both_member(r, team_id, user_id_sender, user_id_receiver):
    sender_ok = is_member(r, team_id, user_id_sender)
    receiver_ok = is_member(r, team_id, user_id_receiver)

    return sender_ok and receiver_ok
