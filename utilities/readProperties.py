"""module for working with INI files."""
import configparser

# create a obj for call .ini file
config=configparser.RawConfigParser()
config.read(".\\Config\\config.ini")

# get data from config.ini
class ReadConfig:
    @staticmethod #directed acces fun using class name
    # from url
    def getApplicationURL():
        url=config.get('common info for admin login','baseURL')
        return url


    @staticmethod
    # from username
    def getUsername():
        username = config.get('common info for admin login', 'username')
        return username

    @staticmethod
    # from password
    def getPassword():
        password = config.get('common info for admin login', 'password')
        return password


