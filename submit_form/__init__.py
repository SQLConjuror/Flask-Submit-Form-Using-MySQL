from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector
import os


app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)

_config = {
    'user': '<your_db_user>',
    'password': '<db_user_password>',
    'host': '<db_host>',
    'database': '<database>',
    'raise_on_warnings': True,
    }
cnx = mysql.connector.connect(**_config)


from submit_form import routes
