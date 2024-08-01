from flask import Flask
from flask import request
from flask import jsonify
import requests
import sqlalchemy

app=Flask(__name__)

@app.route('/api/v1/track/<id>/',methods=['POST','GET'])
def track(id):
    ip_address = request.remote_addr
    print(ip_address)
    location_info = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
    country = location_info.get('country')
    city = location_info.get('city')

    print(country,city)
    return ""
    

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
   