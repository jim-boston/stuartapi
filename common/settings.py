import os
from common.decorators import singleton


@singleton
class Settings(object):

    def __init__(self):
        self.username = (os.environ.get('STUARTAPI_DBUSERNAME') if os.environ.get('STUARTAPI_DBUSERNAME') != None else "sa")
        self.password = (os.environ.get('STUARTAPI_DBPASSWORD') if os.environ.get('STUARTAPI_DBPASSWORD') != None else "tpifSA!2024")
        self.host = (os.environ.get('STUARTAPI_DBHOST') if os.environ.get('STUARTAPI_DBHOST') != None else "172.16.4.4")
        self.database = (os.environ.get('STUARTAPI_DBNAME') if os.environ.get('STUARTAPI_DBNAME') != None else "TU_Med_OSA")
        self.mode = (os.environ.get('STUARTAPI_MODE') if os.environ.get('STUARTAPI_MODE') != None else "host")

