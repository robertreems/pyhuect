# Registers this app to the Hue and returns the registered username.
# The username is generated automatically by the Hue.
import logging
import requests


class Register:
    hueip = ''
    username = ''

    def __init__(self, hueip):
        self.hueip = hueip
        self.register()

    def register(self):
        url = 'http://' + str(self.hueip) + '/api'
        postdata = '{"devicetype": "MyfirstApp"}'

        response = requests.post(url, data=postdata)
        json = response.json()

        if 'error' in json[0]:
            raise RuntimeError(json[0]['error']['description'])
        elif 'success' in json[0]:
            logging.info('success!')
            self.username = json[0]['success']['username']
