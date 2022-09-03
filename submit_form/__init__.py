from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector
import os


app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SECRET_KEY'] = os.urandom(24)
Bootstrap(app)

_config = {
    'user': 'smartlink@test-smartlink-data-extraction',
    'password': 'Supp0rt#12',
    'host': 'test-smartlink-data-extraction.mysql.database.azure.com',
    'database': 'employee_data',
    'raise_on_warnings': True,
    }
cnx = mysql.connector.connect(**_config)


from submit_form import routes