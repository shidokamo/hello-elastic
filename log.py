import time
import random
import os
from datetime import datetime
from geopy.geocoders import Nominatim
import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s : %(message)s',
        },
        'ltsv': {
            'format': 'time:%(asctime)s\tlevel:%(levelname)s\t%(message)s',
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
            'formatter': 'ltsv',
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

console.info("------------------------------------------------------------------")
console.info(" logging : interval = {} sec".format(os.environ.get('LOG_INTERVAL')))
console.info("------------------------------------------------------------------")
i = 0
geolocator = Nominatim(user_agent="app")
category_index = list(range(10))
while True:
    # Generate random longitude and latitude
    lat = round(random.uniform(0, 90), 6)
    lon = round(random.uniform(0, 90), 6)
    console.info("[{:8}] Latitude: {}, Longitude: {}".format(i, lat, lon))
    try:
        location = geolocator.reverse("{}, {}".format(lat, lon))
        # Add some random values
        location.raw['cost'] = random.gauss(500, 100)
        location.raw['score'] = random.random()
        location.raw['category'] = random.sample(category_index, k=1)[0]
        fwrite.info(location.raw) # Dump raw JSON into the file
    except Exception as e:
        console.warning(e);
    if os.environ.get('LOG_INTERVAL'):
        time.sleep(float(os.environ['LOG_INTERVAL']))
    i += 1
