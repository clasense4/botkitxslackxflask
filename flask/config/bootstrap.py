from flask import Flask
import redis

app = Flask(__name__)
app.config.from_object('config.env.Dev')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

URL_PREFIX = '/v1'
APP_KEY = '313354'