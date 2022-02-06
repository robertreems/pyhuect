import requests
import time
import logging
import colortempschema
from pathlib import PurePath
import os


class lights:
    hueip = ''
    hueconf = ''
    colortempschemafile = PurePath(os.environ['HOME']).joinpath('.hue', 'colortempschema.json')
    schema = colortempschema.colortempschema()
    schema.readschema(colortempschemafile)

    def __init__(self, hueip, hueconf):
        self.hueip = hueip
        self.hueconf = hueconf

        self.setlights()

    def setlights(self):
        # Get and print all lights
        url = 'http://' + str(self.hueip) + '/api/' + self.hueconf.username + '/lights/'
        response = requests.get(url)
        lights = response.json()

        # # The light schema in an hashtable:
        # schema = {
        #     0: '{"ct": 447}',
        #     1: '{"ct": 447}',
        #     2: '{"ct": 447}',
        #     3: '{"ct": 447}',
        #     4: '{"ct": 447}',
        #     5: '{"ct": 300}',
        #     6: '{"ct": 300}',
        #     7: '{"ct": 300}',
        #     8: '{"ct": 233}',
        #     9: '{"ct": 233}',
        #     10: '{"ct": 233}',
        #     11: '{"ct": 233}',
        #     12: '{"ct": 233}',
        #     13: '{"ct": 233}',
        #     14: '{"ct": 233}',
        #     15: '{"ct": 233}',
        #     16: '{"ct": 363}',
        #     17: '{"ct": 363}',
        #     18: '{"ct": 363}',
        #     19: '{"ct": 363}',
        #     20: '{"ct": 447}',
        #     21: '{"ct": 447}',
        #     22: '{"ct": 447}',
        #     23: '{"ct": 447}'
        # }

        current_time = time.localtime()

        for light in lights:
            url = 'http://' + str(self.hueip) + '/api/' + self.hueconf.username + '/lights/' \
                + light + '/state'
            
            colortemp = [x['ct'] for x in self.schema.getschema()['schema'] if x['hour'] == current_time.tm_hour][0]
            lightconfig = '{"ct": ' + str(colortemp) + '}'
            response = requests.put(url, lightconfig)
            json = response.json()
            logging.debug(json)
