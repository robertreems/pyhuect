#!/usr/bin/env python3
# https://github.com/tigoe/hue-control
import ipaddress
import hueconf
import logging
import registerapp
import time
import lights
from pathlib import PurePath
import os
import requests

print('started app')

logging.basicConfig(level=logging.DEBUG)

# Get the configuration from user profile
configfile = PurePath(os.environ['HOME']).joinpath('.hue','hueconf.ini')
hueconf = hueconf.ConfigFile(configfile)

hueip = ipaddress.ip_address(hueconf.hueIp)
try:
    username = hueconf.getusername()
    logging.debug('username {} is set in config file'.format(username))

except:
    logging.debug('username not set in config file')

    try:
        app = registerapp.Register(hueip)
        hueconf.setusername(app.username)
        hueconf.writeconfig()


    except:
        raise ValueError('Failed to register app to Hue.')

while True:
    try:
        lights.lights(hueip, hueconf)
    except Exception as e:
        logging.warning('Unhandled exception: {}'.format(e))
    
    time.sleep(5)
