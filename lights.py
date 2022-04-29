import requests
import time


class lights:
    hueip = ''
    hueconf = ''
    schema = ''  # The light schema from json file.

    def __init__(self, hueip, hueconf, schema):
        self.hueip = hueip
        self.hueconf = hueconf
        self.schema = schema

        self.setlights()

    def setlights(self):
        # Get all lights.
        url = 'http://' + str(self.hueip) + '/api/' + \
            self.hueconf.username + '/lights/'
        response = requests.get(url)
        lights = response.json()

        current_time = time.localtime()

        # Set the state of each light.
        for light in lights:
            url = 'http://' + str(self.hueip) + '/api/' + self.hueconf.username + '/lights/' \
                + light + '/state'

            colortemp = [x['ct'] for x in self.schema.getschema()['schema'] if x['hour']
                         == current_time.tm_hour][0]
            lightconfig = '{"ct": ' + str(colortemp) + '}'
            # todo raise runtime error if response is not 200. Log the error with base.
            response = requests.put(url, lightconfig)
