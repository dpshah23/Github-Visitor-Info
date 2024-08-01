from flask import Flask, request, jsonify
import pymysql
import requests
import pycountry
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

DBNAME = os.getenv('DBNAME')
HOST = os.getenv('HOST')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

print(DBNAME,USERNAME,HOST,PASSWORD)

app = Flask(__name__)

# Database connection setup
connection = pymysql.connect(
    host=HOST,
    user='avnadmin',
    password=PASSWORD,
    database=DBNAME,
    port=18462
)

@app.route('/api/v1/track/<id>/', methods=['POST', 'GET'])
def track(id):
    try:
        with connection.cursor() as cursor:
          
            cursor.execute("SELECT * FROM Users_main WHERE unique_link = %s", (id,))
            user = cursor.fetchone()
            if not user:
                return 'Invalid Link', 404
            
            ip_address = request.remote_addr
            print(ip_address)
            location_info = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
            print(location_info)
            if location_info.get('bogon'):
                return ""
            
            country_code = location_info.get('country')
            state = location_info.get('region')
            city = location_info.get('city')

            country_name = None
            try:
                country_name = pycountry.countries.get(alpha_2=country_code).name
            except (AttributeError, LookupError):
                country_name = country_code

            # Insert visit record
            cursor.execute(
                "INSERT INTO Visits (unique_link, city, state, country, timestamp) VALUES (%s, %s, %s, %s, %s)",
                (id, city, state, country_name, datetime.now())
            )
            connection.commit()

            print(country_name, city, state)
            return '', 200
    except Exception as e:
        print(f"Error: {e}")
        return "", 500

