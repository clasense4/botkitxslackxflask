from config.bootstrap import app
from config.bootstrap import URL_PREFIX
from controllers import slack_controller

slack = slack_controller.slack_controller()
app.add_url_rule(URL_PREFIX+'/karma/send', methods=['POST'], view_func=slack.karma_send)
app.add_url_rule(URL_PREFIX+'/karma/remaining', methods=['POST'], view_func=slack.karma_remaining)
app.add_url_rule(URL_PREFIX+'/leaderboard', methods=['POST'], view_func=slack.leaderboard)
app.add_url_rule(URL_PREFIX+'/signup', methods=['POST'], view_func=slack.signup)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
