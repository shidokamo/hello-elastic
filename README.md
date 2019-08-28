# Hello Elastic
Elasticsearch + Kibana を動かしてみるサンプルです。

## インストール
Elasticsearch をいずれかの方法でインストールしてください。

Makefile を使ってインストールする場合は、

```
make install
```

## Kibana の設定
Kibana の設定ファイルを変更します。
Makefile からインストールした場合は、`${KIBANA_HOME}/config/kibana.yml` を編集してください。

nginx のベーシック認証を使う場合は、
```
server.host: "localhost"
server.name: "kibana"
elasticsearch.hosts: ["http://localhost:9200"]
```

## Elasticsearch の起動
```
make elasticsearch
```

## Kibana  の起動
```
make kibana
```

