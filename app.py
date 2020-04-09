from flask import Flask
from flask import jsonify
from logging.config import fileConfig
import logging
import json
import traceback

class FormatterJSON(logging.Formatter):
    def format(self, record):
        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)

        json_log = {
            'levelname': record.levelname,
            'time': '%(asctime)s.%(msecs)dZ' % dict(asctime=record.asctime, msecs=record.msecs),
            'aws_request_id': getattr(record, 'aws_request_id', '00000000-0000-0000-0000-000000000000'),
            'message': record.message,
            'module': record.module,
            'extra_data': record.__dict__.get('data', {}),
        }
        
        if record.stack_info:
            json_log.stack_info = record.stack_info
            
        return json.dumps(json_log)

fileConfig('./logging.conf')

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_invalid_usage(error):
    error_string = traceback.format_exc()
    app.logger.error(error_string)

    return error

@app.route('/')
def homepage():
    return 'Hello There!'

@app.route('/info')
def info_message():
    app.logger.info("""INFO LOGGING MESSAGE
    
    ACCROSS MULTIPLE LINES!?!
    """)
    app.notamethod()
    return 'Logging Info Message!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')