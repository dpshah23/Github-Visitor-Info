from flask import Flask
from flask import request
from flask import jsonify
import requests
import sqlalchemy
from models import Visits
import pycountry
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

load_dotenv()

DBNAME=os.getenv('DBNAME')
HOST=os.getenv('HOST')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DBNAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/api/v1/track/<id>/',methods=['POST','GET'])
def track(id):
    ip_address = request.remote_addr
    print(ip_address)
    location_info = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
    if location_info.get('bogon'):
        return "private ip address"
    country = location_info.get('country')
    state=location_info.get('region')
    city = location_info.get('city')
    try:
        country = pycountry.countries.get(alpha_2=country)
    except LookupError:
        pass

    visit = Visits(
        unique_link=id,
        city=city,
        state=state,
        country=country,
        timestamp=datetime.now()
    )
    db.session.add(visit)
    db.session.commit()

    print(country,city,state)
    return ""
    

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)
   