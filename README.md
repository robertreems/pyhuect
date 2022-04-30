# Pyhuect
The program is designed to set the color temperature of all my Philips lights based on the hour of the day.

The program has been build to run on Linux. It's been tested on Ubuntu 20.04 and Raspbian 11.

## first usage
Create the lights schema file in file ~/.hue/colortempschema.json. The file should have the following schema:
```
{
    "schema":[
        {"hour":0, "ct": 447},
        {"hour":1, "ct": 447},
        {"hour":2, "ct": 447},
        {"hour":3, "ct": 447},
        {"hour":4, "ct": 447},
        {"hour":5, "ct": 300},
        {"hour":6, "ct": 300},
        {"hour":7, "ct": 300},
        {"hour":8, "ct": 233},
        {"hour":9, "ct": 233},
        {"hour":10, "ct": 233},
        {"hour":11, "ct": 233},
        {"hour":12, "ct": 233},
        {"hour":13, "ct": 233},
        {"hour":14, "ct": 233},
        {"hour":15, "ct": 233},
        {"hour":16, "ct": 363},
        {"hour":17, "ct": 363},
        {"hour":18, "ct": 363},
        {"hour":19, "ct": 363},
        {"hour":20, "ct": 447},
        {"hour":21, "ct": 447},
        {"hour":22, "ct": 447},
        {"hour":23, "ct": 447}
    ]
}
```

Just hit the link button on the Hue bridge and start the program. During the first execution a configuration file will be created: ~/.hue/hueconf.ini. This INI file contains 2 sections:
1. [Hue]
This section has the IP key. You can set this yourself. But aren't obligated to do so.

2. [DONOTEDIT]
This section is fully managed by the program. Do not edit it yourself unless you know the username and want to set it yourself.

# Usage of the program
As stated before, you'll have to execute the main.py file.

# A note from Robert
I've made this project primarily to learn coding Python. I'll probably abandon the project in the near future. You should do as well as there are far better alternatives.
For example: https://github.com/aleroddepaz/pyhue

I might add future features like:
- Pausing the program.
- Web interface
- Parameterized configuration

Furthermore I like to learn more about Python code quality and best practices. So expect frequent refactoring without providing new functionality.