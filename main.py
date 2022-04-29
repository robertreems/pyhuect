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
import cli
import colortempschema

print('started app')

cli = cli.cliclass()

if cli.args.verbose:
    # Set the root loggig level
    logger = logging.getLogger()  # get the root
    logger.setLevel(logging.DEBUG)

# Get the configuration from user profile
configfile = PurePath(os.environ['HOME']).joinpath('.hue', 'hueconf.ini')
hueconf = hueconf.ConfigFile(configfile)

hueip = ipaddress.ip_address(hueconf.hueIp)

username = hueconf.getusername()

colortempschemafile = PurePath(os.environ['HOME']).joinpath('.hue', 'colortempschema.json')
schema = colortempschema.colortempschema()
schema.readschema(colortempschemafile)

if username:
    username = hueconf.getusername()
    logging.debug('username {} is set in config file'.format(username))

else:
    logging.debug('Registering username in config file')

    app = registerapp.Register(hueip)
    hueconf.setusername(app.username)
    hueconf.writeconfig()

while True:
    try:
        lights.lights(hueip, hueconf, schema)
    except Exception as e:
        logging.warning('Unhandled exception: {}'.format(e))

    time.sleep(5)
