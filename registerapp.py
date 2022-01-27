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
        logging.info('registering on {}'.format(self.hueip))
        url = 'http://' + str(self.hueip) + '/api'
        postdata = '{"devicetype": "MyfirstApp"}'

        response = requests.post(url, data=postdata)
        json = response.json()

        if 'error' in json[0]:
            raise ValueError(json[0]['error']['description'])
        elif 'success' in json[0]:
            logging.info('success!')
            self.username = json[0]['success']['username']

            # url = 'http://' + str(self.hueip) + '/api/' + username
            # response = requests.get(url)
            # json = response.json()
            # logging.info(json)

            logging.debug('registered user: {}'.format(self.username))
