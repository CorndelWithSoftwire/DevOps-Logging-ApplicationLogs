from flask import Flask
import logging
 
app = Flask(__name__)
 
@app.route('/error_page')
def log_an_error():
    app.logger.log(logging.ERROR, "Something really bad happened!")
    return 'Logged Error!'
 
app.run()