~/redis-4.0.6/src/redis-cli < bootstrap_redis
rm -rf .coverage
nosetests test/test_karma.py --with-coverage --cover-package=controllers,utils,decorators --cover-html