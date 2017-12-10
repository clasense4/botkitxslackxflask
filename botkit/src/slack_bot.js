if (!process.env.token) {
    console.log('Error: Specify token in environment');
    process.exit(1);
}

var Botkit = require('../lib/Botkit.js');
var os = require('os');
var axios = require('axios');
var querystring = require('querystring');

var slackApi = axios.create({
  baseURL: 'http://localhost:5000/v1/',
  timeout: 1000,
  headers: {'X-App-Key': '123123123', 'Content-Type': 'application/x-www-form-urlencoded'}
});

var controller = Botkit.slackbot({
    debug: true,
});

var bot = controller.spawn({
    token: process.env.token
}).startRTM();

controller.hears(['leaderboard'],'direct_mention,mention,direct_message', function(bot, message) {
    slackApi.post('/leaderboard', querystring.stringify({
        team_id: message.team
      }))
      .then(function (response) {
        console.log(response.data.data);
        if (response.data.data.length > 0) {
            msg = 'Leaderboard\n\n';
            for (var i = 0; i < response.data.data.length; i++) {
                console.log(response.data.data[i]);
                msg += print_id(response.data.data[i][0]) + response.data.data[i][1] + ' Points\n';
            }
            bot.reply(message, msg);
        } else {
            bot.reply(message, 'No activities yet.');
        }
      })
      .catch(function (error) {
        console.log(error);
      });
});

controller.hears(['karma'],'direct_message', function(bot, message) {
    slackApi.post('/karma/remaining', querystring.stringify({
        team_id: message.team,
        user_id: message.user
      }))
      .then(function (response) {
        points = response.data.data.karma;
        msg = 'Karma Points Count = ' + response.data.data.karma_points_count + '\n';
        msg += 'Karma Points Given = ' + response.data.data.karma_points_given + '\n';
        msg += 'Karma Points Lefts = ' + response.data.data.karma_points_remaining + '\n';
        bot.reply(message, msg);
      })
      .catch(function (error) {
        console.log(error);
      });
});

controller.middleware.categorize.use(function(bot, message, next) {
    if (message.type == 'ambient') {
        target = target_match(message.text);

        if (null !== target) {
            // TODO : Match multiple users
            target_user_raw = find_users(target[0])[0];
            target_user = target_user_raw.replace('<','').replace('@','').replace('>','')

            // User cannot send karma to themself
            if (message.user != target_user) {
                slackApi.post('/karma/send', querystring.stringify({
                    team_id: message.team,
                    user_id_from: message.user,
                    user_id_target: target_user,
                  }))
                  .then(function (response) {
                    if (response.data.data.message == 'Not enough karma') {
                        bot.whisper(message, {as_user: true, text: 'Not enough karma. Please try again tomorrow.'});
                    } else {
                        msg = print_id(target_user) + ' receives 1 point from '+print_id(message.user)+'.\n';
                        msg += 'He now has '+response.data.data.target.karma_count+' points.';
                        bot.reply(message, msg);
                    }
                  })
                  .catch(function (error) {
                    console.log(error);
                  });
            } else {
                bot.whisper(message, {as_user: true, text: 'You can not send karma point to yourself.'});
            }
        }
    }
    next();
});

// Regex to match user mention
// ex : thanks @fajri
function target_match(text) {
    var re = /thanks <@.*>/gi;
    var found = text.match(re);

    return found;
}

function find_users(text) {
    var re = /<@.*>/gi;
    var found = text.match(re);

    return found;
}

function print_id(user_id) {
    return '<@'+user_id+'>';
}