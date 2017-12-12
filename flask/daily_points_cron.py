"""
Set Daily points to all member

* List from redis members sets
* Loop each of it
* Set redis key with value 5
"""

from config.bootstrap import r, DAILY_KARMA
team_id = 'T89MU6P6G'

users = r.smembers(team_id+':'+'members')

for user in users:
	r.set(team_id+':'+user+':karma:today', DAILY_KARMA)
