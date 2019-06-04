class Config:
    SECRET_KEY = 'de104ecad906b0ca18ef455a25c32172'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =os.environ.get('EMAIL_PASS')
