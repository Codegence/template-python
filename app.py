#!flask/bin/python

#    Copyright (C) 2014  Gabriel Flores
#    This file is part of Codegence.
#
#    Codegence is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Codegence is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Codegence. If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello to Python Codegence!"

@app.route('/info')
def info():
    return jsonify({'version':'1.1.0'})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/recyclers/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnRecycler(sectorId, factionId, id):	
    print request.json
    return jsonify({'command': random.choice(['newDrone', 'newTerminator']), 'value':0.0})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/drones/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnDrone(sectorId, factionId, id):
    print request.json
    return jsonify({'command':random.choice(['advance', 'rotate']), 'value':10.0})

@app.route('/sectors/<int:sectorId>/factions/<int:factionId>/terminators/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def eventOnTerminator(sectorId, factionId, id):
    print request.json
    return jsonify({'command':random.choice(['advance', 'rotate', 'fire']), 'value':10.0})

if __name__ == '__main__':
	port = int(os.environ.get('PORT',5000))
	app.run( host='0.0.0.0', port=port, debug=True)