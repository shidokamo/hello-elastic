# Hello Elastic
Elasticsearch + Kibana を動かしてみるサンプルです。

## データ（アメリカの座標）
ランダムに生成した位置情報を出力します。
領域判定に使う geojson データとして、
http://eric.clst.org/tech/usgeojson/
を用いています。

オリジナルのデータは、The Census Bureau によって生成されました。

## データ（日本の座標）
簡略化した日本の geojson データとして、以下のものを用いさせていただきました。
https://gist.github.com/shimizu/627b37e303efaf4045f637322e9898ee

## インストール
Elasticsearch + Kibana をいずれかの方法でインストールし、設定を行い、起動してください。
Elasticsearch は、localhost:9200 である必要があります。

## elasticsearch のマッピングの設定
```
make elastic
```

## fluentd の起動
ローカルのファイルを入力として、起動します。
```
make fluentd
```

## Python からログを吐く
ファイルローテートを行いながら、ログをファイルに記録し続けます。
```
make log LOG_INTERVAL=1  # Slow rate
make log                 # Max rate
```

