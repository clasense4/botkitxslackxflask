# Botkit x Slack x Flask

## Introduction

Building bot via botkit library and flask microframework to provide data.

## Features

1. User can invite bot to channel
2. User can signup to play with bot
3. User can see their points, and given points
4. User can give points to another (but limited)
5. User can see leaderboard
6. *Bot can only give points if both user in same channel

## Requirements

- NodeJS 8.9.3
- NPM 5.5.1
- Python 2.7.12
- Python pip
- Python Virtualenv
- Redis 4.0.6
- Linux Server

## Installation

### Redis

```
wget http://download.redis.io/releases/redis-4.0.6.tar.gz
tar xzf redis-4.0.6.tar.gz
cd redis-4.0.6
make
src/redis-server
```

### Python

```
mkdir ~/Envs
which python
# Make sure python interpreter is correct
virtualenv -p /usr/local/bin/python2.7 ~/Envs/botkitxslackxflask

# If virtualenvwrapper not installed
source ~/Envs/botkitxslackxflask/bin/activate

cd ~/botkitxslackxflask
cd flask
pip install -r requirements.txt

# Run webserver
(botkitxslackxflask) root➜~/botkitxslackxflask/flask» python main.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 316-121-414
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
token=xoxb-axcasdas node slack_bot.js
```


## Test

### Python

>>> Make sure redis is running

```
$> sh test.sh
OK
..............
Name                              Stmts   Miss  Cover
-----------------------------------------------------
controllers/__init__.py               0      0   100%
controllers/slack_controller.py      54      0   100%
decorators/__init__.py                0      0   100%
decorators/headers.py                16      0   100%
utils/__init__.py                     0      0   100%
utils/redis_util.py                  20      0   100%
utils/response_util.py               10      0   100%
-----------------------------------------------------
TOTAL                               100      0   100%
----------------------------------------------------------------------
Ran 14 tests in 0.085s

OK
