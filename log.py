import time
import random
import os
import json
from datetime import datetime
from geopy.geocoders import Nominatim
import logging
from logging.config import dictConfig
from shapely.geometry import shape, Point

dictConfig({
    'version': 1,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s : %(message)s',
        },
        'ltsv': {
            'format': 'time:%(asctime)s\tlevel:%(levelname)s\t%(message)s',
        },
        'json': {
            #  TODO: 構造化データの中に、level などの情報を入れたいのだがやり方がわからない。
            # 'format': "{'time':'%(asctime)s','level':'%(levelname)s','data':%(message)s}",
            'format': "%(message)s",
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'file-rotate': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'json',
            'filename': 'app.log',
            'interval': 5,
            'when': 'S',
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'file': {
            'level': 'DEBUG',
            'handlers': ['file-rotate'],
        },
        'console': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
#    'root': {
#        'level': 'DEBUG',
#        'handlers': ['console'],
#    },
})

console = logging.getLogger('console')
fwrite  = logging.getLogger('file')

SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
GEO_JSON_PATH = SOURCE_PATH + "/gz_2010_us_outline_20m.json"
GEO_JSON = json.load(open(GEO_JSON_PATH,'r'))

# 任意の位置情報がアメリカに属するかどうか確認するメソッド
# Usage : usa_region(34.699134, 135.495218)
def usa_region(lat, lon):
    point = Point(lon, lat) # GEO_JSON uses unusual (lon, lat) order !!
    for feature in GEO_JSON['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return True
    return False

console.info("------------------------------------------------------------------")
console.info(" logging : interval = {} sec".format(os.environ.get('LOG_INTERVAL')))
console.info("------------------------------------------------------------------")
i = 0
category_index = list(range(10))
while True:
    # Generate random longitude and latitude
    lat = round(random.uniform(-90, 90), 6)
    lon = round(random.uniform(-180, 180), 6)
    console.info("[{:8}] Latitude: {}, Longitude: {}".format(i, lat, lon))
    try:
        if usa_region(lat, lon):
            data = {
                    'lat': lat,
                    'lon': lon,
                    # Add some random values
                    'cost': random.gauss(500, 100),
                    'score': random.random(),
                    'category': random.sample(category_index, k=1)[0],
                    }
            fwrite.info(json.dumps(data)) # Dump raw JSON into the file
        else:
            console.info("Latitude: {}, Longitude: {} is not in USA region".format(lat, lon))
    except Exception as e:
        console.warning(e);
    if os.environ.get('LOG_INTERVAL'):
        time.sleep(float(os.environ['LOG_INTERVAL']))
    i += 1
