from configparser import ConfigParser
import os

config_path = os.path.join(os.path.dirname(os.getcwd()), 'workshop.conf')
def read_config():
    parser = ConfigParser()
    parser.read([config_path])
    return parser
    