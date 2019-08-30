# Hello Elastic
Elasticsearch + Kibana を動かしてみるサンプルです。

## データ
ランダムに生成したアメリカ内の位置情報を出力します。
領域判定に使う geojson データとして、
http://eric.clst.org/tech/usgeojson/
を用いています。

オリジナルのデータは、The Census Bureau によって生成されました。

## インストール
Elasticsearch + Kibana をいずれかの方法でインストールし、設定を行い、起動してください。
Elasticsearch は、localhost:9200 である必要があります。

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




