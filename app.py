import logging
from flask import Flask
from logging.config import fileConfig
 
fileConfig('./logging.conf')
 
app = Flask(__name__)

@app.route('/')
def homepage_with_info_log():
    app.logger.info("Something not as serious")
    return 'Logged Info Message'
 
@app.route('/error_page')
def log_an_error():
    app.logger.log(logging.ERROR, "Something really bad happened!")
    return 'Logged Error!'
 
app.run()