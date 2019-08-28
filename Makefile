ELASTIC_VERSION=7.3.1

install:install-elasticsearch
install-elasticsearch:
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
	shasum -a 512 -c elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512
	tar -xzf elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	rm elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz
	rm elasticsearch-${ELASTIC_VERSION}-linux-x86_64.tar.gz.sha512

