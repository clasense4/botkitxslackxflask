"""
Config file for various database connection
"""
class Prod():
    # Redis Configuratioin
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0

class Dev():
    DEBUG = True

    # Redis Configuratioin
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0

class Test():
    TESTING = True
    DEBUG = True

    # Redis Configuratioin
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0

class Local():
    DEBUG = True

    # Redis Configuratioin
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0