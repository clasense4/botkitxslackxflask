~/redis-4.0.6/src/redis-cli < bootstrap_redis
source ~/Envs/botkitxslackxflask/bin/activate
rm -rf .coverage
nosetests test/test_karma.py --with-coverage --cover-package=controllers,utils,decorators --cover-html --logging-level=DEBUG
#nosetests test/test_karma.py --with-coverage --cover-package=controllers,utils,decorators --logging-level=DEBUG -l debug
