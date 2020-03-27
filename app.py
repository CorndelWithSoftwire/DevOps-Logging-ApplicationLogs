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
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')