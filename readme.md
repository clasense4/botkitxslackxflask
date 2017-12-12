# Botkit x Slack x Flask

## Introduction

Building slack bot via [botkit](https://github.com/howdyai/botkit) library and [flask](https://github.com/pallets/flask) microframework to provide data.

### Why Flask and not express or "just code the logic there"?

Currently, I have no experience with nodejs express. And I have some experience with flask, and possible to achieve 100% coverage.

Well, previously I try to code inside botkit, but I think it will be better if I split with another service. In production, we can split those to different services, like utilizing AWS Lambda & Api Gateway for REST API. So, if REST API Service is down, the bot is not down, even it cannot use interactively, let say, the bot can send log to message pipline.

### Why Redis

Redis will be use as primary data store. `String`, `Hash`, `Sets`, `Sorted Sets` Data Types is used.

Example :

```
1) "T89MU6P6G:U8917CU0Y:karma:today" => String
2) "T89MU6P6G:U8917CU0Y" => Hash
3) "T89MU6P6G:U8BHP3V1D:karma:today" => String
4) "T89MU6P6G:U8BHP3V1D" => Hash
5) "T89MU6P6G:members" => Sets
6) "T89MU6P6G:leaderboard" => Sorted Sets
```

I think Redis is the easiest way to achieve goal of this projects and Redis is fast. 

## Features

1. User can invite bot to channel
2. User can signup to play with bot
3. User can see their points and given points
4. User can give points to another (limited)
5. User can see leaderboard

## Requirements

- NodeJS 8.9.3
- NPM 5.5.1
- Python 2.7.12
- Python pip
- Python Virtualenv
- Redis 4.0.6
- Linux Server
- Slack Team
- [Slack Bot Token](https://github.com/howdyai/botkit/blob/master/docs/readme-slack.md#getting-started)

## Installation

### Redis

```
wget http://download.redis.io/releases/redis-4.0.6.tar.gz
tar xzf redis-4.0.6.tar.gz
cd redis-4.0.6
make
# Run Redis server
src/redis-server
```

### Python

```
mkdir ~/Envs
which python
# Make sure python interpreter is correct
virtualenv -p /usr/local/bin/python2.7 ~/Envs/botkitxslackxflask

# Activate virtualenv
source ~/Envs/botkitxslackxflask/bin/activate

cd ~/botkitxslackxflask
cd flask
pip install -r requirements.txt

# Run webserver
(botkitxslackxflask) root➜~/botkitxslackxflask/flask» python main.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

### Nodejs

```
cd ~
wget https://nodejs.org/dist/v8.9.3/node-v8.9.3-linux-x64.tar.xz
tar xf node-v8.9.3-linux-x64.tar.xz
alias node='/root/node-v8.9.3-linux-x64/bin/node'
alias npm='/root/node-v8.9.3-linux-x64/bin/npm'

git clone ...
cd botkitxslackxflask
cd botkit
npm install

cd src

# Start the bot, change with your slack token
# Read more at https://github.com/howdyai/botkit/blob/master/docs/readme-slack.md#getting-started
token=xoxb-axcasdas node slack_bot.js
```


## Test

### Python

> Make sure redis is running

```
$> sh test.sh
OK
................
Name                              Stmts   Miss  Cover
-----------------------------------------------------
controllers/__init__.py               0      0   100%
controllers/slack_controller.py      59      0   100%
decorators/__init__.py                0      0   100%
decorators/headers.py                16      0   100%
utils/__init__.py                     0      0   100%
utils/redis_util.py                  20      0   100%
utils/response_util.py               10      0   100%
-----------------------------------------------------
TOTAL                               105      0   100%
----------------------------------------------------------------------
Ran 16 tests in 0.164s

OK
