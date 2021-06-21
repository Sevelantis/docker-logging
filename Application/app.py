import os
import logging
import string
import math
import time
import socket


from flask import Flask, request, jsonify
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(name)s:%(message)s')
"""
when writing logs to file - logs doesnt show up in Grafana. Takes STDOUT as source.
"""
# logging.basicConfig(filename='Application.log', level=logging.INFO,
#                     format='%(asctime)s:%(name)s:%(message)s')

app = Flask(__name__)


@app.route("/")
def slash():
    return "/factorial/4 \t->\t factorial of 4 = 1*2*3*4<br> \
        /pow/2^4 \t->\t 2^4 = 16<br> \
        /sqrt/324 \t->\t sqrt{324} = 18<br>"
    # return "/factorial/4 - factorial of 4 = 1*2*3*4<br> /pow/2^4 - 2^4 = 16<br> /sqrt/324 - sqrt{324} = 18<br>"

@app.route("/factorial/<number_in>")
def factorial(number_in):
    number_in = int(number_in)

    start = time.time_ns()            # start time
    number_out = math.factorial(number_in)    
    end = time.time_ns()  
    diff = (end - start)/1000000
    
    msg = f'{str(number_in)}! = {str(number_out)}, calc_time={str(diff)}[ms]'
    logging.info(msg)
    return msg

@app.route("/sqrt/<number_in>")
def sqrt(number_in):
    number_in = int(number_in)

    start = time.time_ns()            # start time
    number_out = math.sqrt(number_in)    
    end = time.time_ns()  
    diff = (end - start)/1000000
    
    msg = f'sqrt2 of {str(number_in)} = {str(number_out)}, calc_time={str(diff)}[ms]'
    logging.info(msg)
    return msg

@app.route("/pow/<number_in>^<power_in>")
def power(number_in, power_in):
    number_in = int(number_in)
    power_in = int(power_in)

    start = time.time_ns()            # start time
    number_out = math.pow(number_in, power_in)    
    end = time.time_ns()  
    diff = (end - start)/1000000
    
    msg = f'{str(number_in)}^{str(power_in)} = {number_out}, calc_time={str(diff)}[ms]'
    
    logging.info(msg)
    return msg


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
