ELASTIC_VERSION=7.3.1
LOG_INTEVAL =
export

log:
	pipenv run python -u log.py
clean:
	-rm -rf *.log*
fluentd:
	bundler exec fluentd -c fluent.conf

install:install-elasticsearch install-kibana install-python install-ruby
install-python:
	pipenv install
install-ruby:
	bundler install
install-elasticsearch:
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
	shasum -a 512 -c elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
	tar -xzf elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	rm elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	rm elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
install-kibana:
	wget https://artifacts.elastic.co/downloads/kibana/kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	# wget https://artifacts.elastic.co/downloads/kibana/kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
	# shasum -a 512 -c kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	tar -xzf kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	rm kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	# rm kibana-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
run-elastic:
	elasticsearch-${ELASTIC_VERSION}/bin/elasticsearch
run-kibana:
	kibana-${ELASTIC_VERSION}-linux-x86_64/bin/kibana
	
