#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello to Python Codegence!"

@app.route('/info')
def info():
	return jsonify({'version':'1.1.0'})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/recyclers/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnRecycler(sectorId, factionId, id):
	return jsonify({'command':'newDrone', 'value':0.0})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/drones/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnDrone(sectorId, factionId, id):
	return jsonify({'command':'advance', 'value':10.0})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/terminators/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnTerminator(sectorId, factionId, id):
	return jsonify({'command':'rotate', 'value':10.0})

if __name__ == '__main__':
    app.run(host='172.17.226.73', debug=True)