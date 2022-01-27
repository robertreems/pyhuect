# My first class
# inspired by: https://www.w3schools.com/python/python_classes.asp

from configparser import ConfigParser
from pathlib import Path
import logging


class ConfigFile:
    hueIp = ''
    config_object = ''
    path = ''
    username = ''

    def __init__(self, path):
        self.path = path

        configfile = Path(path)

        if configfile.exists():
            logging.debug('configfile {} exists'.format(path))
            self.readconfig()
        else:
            logging.debug('configfile {} does not exists'.format(path))
            self.hueIp = input('Enter the hue IP\n')
            self.writeconfig()

    def readconfig(self):
        logging.debug('readconfig started with file {}'.format(self.path))

        self.config_object = ConfigParser()
        self.config_object.read(self.path)

        hueinfo = self.config_object["Hue"]
        self.hueIp = hueinfo["ip"]

        try:
            if "DONOTEDIT" in self.config_object:
                donotedit = self.config_object["DONOTEDIT"]
                self.username = donotedit["username"]
        except KeyError:
            logging.warning('Could not read DONOTEDIT section')
            self.username = ''

    def getusername(self):
        self.readconfig()

        return self.username

    def setusername(self, username):
        self.username = username
        self.writeconfig()

    def writeconfig(self):
        self.config_object = ConfigParser()

        # Hue config section
        self.config_object["Hue"] = {
            "ip": self.hueIp
        }
        # DONOTEDIT config section. This contains the dynamic username
        if self.username:
            self.config_object["DONOTEDIT"] = {
                "username": self.username
            }

        # Create parent directory
        configfile = Path(self.path)
        configfile.parent.mkdir(exist_ok=True)

        # Write the config section to file
        with open(self.path, 'w') as conf:
            self.config_object.write(conf)
