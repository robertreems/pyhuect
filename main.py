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
from colortempschema import Colortempschema
from rvrbase import Rvrbase

from constants import CONFIG_FILE, ERR_READING_COLOR_TEMPS_SCHEMA, ERR_REGISTERING_USER,\
    ERR_UPDATING_HUE_BRIDGE, MSG_REGISTERING_USER, MSG_USERNAME_FOUND

base = Rvrbase(CONFIG_FILE)
cli = cli.cliclass()
schema = Colortempschema()

if cli.args.verbose:
    # Set the root loggig level
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

# Get the configuration from user profile
configfile = PurePath(os.environ['HOME']).joinpath('.hue', 'hueconf.ini')
hueconf = hueconf.ConfigFile(configfile)
hueip = ipaddress.ip_address(hueconf.hueIp)
username = hueconf.getusername()

colortempschemafile = PurePath(os.environ['HOME']).joinpath(
    '.hue', 'colortempschema.json')

try:
    schema.readschema(colortempschemafile)
except Exception as error:
    base.log_app_event(type='error', message=ERR_READING_COLOR_TEMPS_SCHEMA.format(
        file=colortempschemafile, error=error))
    raise RuntimeError(error)

if username:
    base.log_app_event(
        type='info', message=MSG_USERNAME_FOUND.format(username=username))

else:
    base.log_app_event(type='info', message=MSG_REGISTERING_USER)

    try:
        app = registerapp.Register(hueip)
        hueconf.setusername(app.username)
        hueconf.writeconfig()
    except RuntimeError as error:
        base.log_app_event(type='error', message=ERR_REGISTERING_USER.format(
            file=configfile, error=error))

while True:
    try:
        lights.lights(hueip, hueconf, schema)
    except Exception as error:
        base.log_app_event(
            type='warning', message=ERR_UPDATING_HUE_BRIDGE.format(error=error))

    time.sleep(5)
