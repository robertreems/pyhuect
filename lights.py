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

        current_time = time.localtime()

        for light in lights:
            url = 'http://' + str(self.hueip) + '/api/' + self.hueconf.username + '/lights/' \
                + light + '/state'

            colortemp = [x['ct'] for x in self.schema.getschema()['schema'] if x['hour']
                         == current_time.tm_hour][0]
            lightconfig = '{"ct": ' + str(colortemp) + '}'
            response = requests.put(url, lightconfig)
            json = response.json()
            logging.debug(json)
