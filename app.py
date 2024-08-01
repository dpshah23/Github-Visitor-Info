from flask import Flask
from flask import request
from flask import jsonify
import requests
import sqlalchemy

app=Flask(__name__)

@app.route('/api/v1/track/<id>/',methods=['POST','GET'])
def track(id):
    return "Tracked"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
   