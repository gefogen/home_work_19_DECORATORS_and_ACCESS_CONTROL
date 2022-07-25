# Это файл конфигурации приложения, здесь может храниться путь к бд, ключ шифрования, что-то еще.

class Config:
     SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
     SQLALCHEMY_TRACK_MODIFICATIONS = False
     RESTX_JSON = {'ensure_ascii': False}
     DEBUG = True
     SECRET = '249y823r9v8238r9u'
