# Pyhuect
The program is designed to set the color temperature of all my Philips lights based on the hour of the day.

The program has been build to run on Linux. It's been tested on Ubuntu 20.04 and Raspbian.

Just start run the main.py file to start the program.

A configuration file will be created: ~/.hue/hueconf.ini. This INI file contains 2 sections:
1. [Hue]
This section has the IP key. You can set this yourself. But aren't obligated to do so.

2. [DONOTEDIT]
This section is fully managed by the program. Do not edit it yourself unless you know the username and want to set it yourself.

## first usage
Just hit the link button on the Hue bridge and start the program.
That's it!

# A note from Robert
I've made this project primarily to learn coding Python. I'll probably abandon the project in the near future. You should do as well as there are far better alternatives.
For example: https://github.com/aleroddepaz/pyhue

I might add future features like:
- Pausing the program.
- Web interface
- Parameterized configuration

Furthermore I like to learn more about Python code quality and best practices. So expect frequent refactoring without providing new functionality.