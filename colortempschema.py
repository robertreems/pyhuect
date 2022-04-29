"""
Reads the colortempschema.json file.
This file contains the color temperature schema per hour of the day for my Philips Hue lights.

Inspired by:
https://www.geeksforgeeks.org/read-json-file-using-python/
"""

import logging
import json


class colortempschema:
    jsoncolortempschema = None

    def readschema(self, schemafilepath):
        logging.debug('reading file: ' + str(schemafilepath))

        schemafile = open(schemafilepath)
        self.jsoncolortempschema = json.load(schemafile)

    def getschema(self):
        if self.jsoncolortempschema is None:
            raise ValueError('var jsoncolortempschema is not set. Call method readschema first.')

        return self.jsoncolortempschema
