ELASTIC_VERSION=7.3.1
LOG_INTEVAL =
export

log:
	pipenv run python -u log.py
clean:
	-rm -rf *.log*
fluentd:
	bundler exec fluentd -c fluent.conf

install:install-python install-ruby
install-python:
	pipenv install
install-ruby:
	bundler install

