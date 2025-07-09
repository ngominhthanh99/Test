import json
import os

class configreader:
    _config = None

    @staticmethod
    def loadconfig():
        if configreader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'setting.json')
            with open(config_path, 'r') as configfile:
                configreader._config = json.load(configfile)
        return configreader._config
    
    @staticmethod
    def get_baseurl():
        return configreader.loadconfig()['baseurl']
    
    @staticmethod
    def get_username():
        return configreader.loadconfig()['credentials']['username']
    
    @staticmethod
    def get_password():
        return configreader.loadconfig()['credentials']['password']
    
    @staticmethod
    def get_timeout():
        timeout_settings = configreader.loadconfig().get('timeout', {})
        return float(timeout_settings.get('implicit', 5))