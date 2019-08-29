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

nginx のベーシック認証を使う場合は、以下のようにローカルホストからの通信のみを許可するように
してください。
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

## Nginx のインストール
無償版では、kibana は起動時に認証を全く行わないので、nginx のベーシック認証を
通して、保護を行うことを推奨します。
詳しくはのちに記載。

## fluentd の起動
ローカルのファイルを入力として、追い続けます。
```
make fluentd
```

## Python からログを吐く
ファイルローテートを行いながら、ログをファイルに記録し続けます。
```
make log LOG_INTERVAL=1  # Slow rate
make log                 # Max rate
```




