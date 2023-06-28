import os
from os import environ

class Config(object):
    '''
    Configuramos el entorno
    '''
    
    DEBUG = False # Deshabilita el modo depuración
    TESTING = False # Deshabilita el modo test
    
    basedir = os.path.abspath(os.path.dirname(__file__)) # Guardamos la ruta del archivo config

    SECRET_KEY = 'jordipg' # Key para firmar cookies

    # Base de datos de guardado
    DB_NAME = "production-db" 
    DB_USERNAME = "root" 
    DB_PASSWORD = "jordipg"

    UPLOADS = "./app/static/uploads" # Ruta de carga de datos

    SESSION_COOKIE_SECURE = True # Cookies seguras
    DEFAULT_THEME = None # No usar tema default

class ProductionConfig(Config):
    '''
    Configuramos entorno de producción (DESACTIVADO)
    '''
    pass

class DevelopmentConfig(Config):
    '''
    Configurar el entorno de desarrollo
    '''
    DEBUG = True # Damos permiso depuración

    # Base de datos de guardado
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "jordipg"

    UPLOADS = "./app/static/uploads" # Ruta de carga de datos
    SESSION_COOKIE_SECURE = False # Utilización de cookies no seguras para desarrollo
    
class TestingConfig(Config):
    '''
    Configurar entorno de testing
    '''
    DEBUG = True # Damos permiso depuración

    # Base de datos de guardado
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "jordipg"

    UPLOADS = "./app/static/uploads"
    SESSION_COOKIE_SECURE = False # Utilización de cookies no seguras para test
    
class DebugConfig(Config):
    DEBUG = False # Deshabilita el modo depuración
 
