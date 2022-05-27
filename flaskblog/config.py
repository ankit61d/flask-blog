import os



class Config:
    # need to make it env variable
   # SECRET_KEY = '8fe443c98a575a84cbac62a78ca69d9095c5479fde467000f7a641e3f2a87cd1'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # 3 slashes are relative file path
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    