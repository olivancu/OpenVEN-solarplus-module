#!flask/bin/python
from flask import Flask, request
import json
app = Flask(__name__)

def print_receive_data(data_type, data_payload):
    print "Receive {} signal from the DR server:".format(data_type)
    print data_payload

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/add-dr-signal/price', methods=["POST"])
def dr_price():
    data = json.loads(request.json)
    print_receive_data("DR PRICE", data['customer_energy_charge'])

    return "ok"

@app.route('/add-dr-signal/shed', methods=["POST"])
def dr_shed():
    data = json.loads(request.json)
    print_receive_data("DR SHED", data)

    return "ok"

@app.route('/add-dr-signal/shift', methods=["POST"])
def dr_shift():
    data = json.loads(request.json)
    print_receive_data("DR SHIFT", data)

    return "ok"

@app.route('/add-dr-signal/limit', methods=["POST"])
def dr_limit():
    data = json.loads(request.json)
    print_receive_data("DR LIMIT", data)

    return "ok"

@app.route('/add-dr-signal/track', methods=["POST"])
def dr_track():
    data = json.loads(request.json)
    print_receive_data("DR TRACK", data)

    return "ok"


if __name__ == '__main__':
    app.run()