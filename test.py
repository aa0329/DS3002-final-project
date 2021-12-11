import mysql.connector
import sqlite3
import requests
import json
import time
import schedule
import requests
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
  host="localhost",
  user="ayushi",
  password="Ayushi29",
  database = "final_data"
)

def job():

    print("I'm working...")

    # preparing a cursor object
    mycursor = mydb.cursor()

    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")

    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
      remote_json = response.json()

    sql = "INSERT INTO pi_data5 (FACTOR, PI, TIMESTAMP) VALUES (%s, %s, %s)"
    val = (remote_json["factor"], remote_json["pi"], remote_json["time"])
    mycursor.execute(sql, val)

    mydb.commit()


schedule.every(1).minutes.until(timedelta(minutes=59)).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# make an array that is powers of i^3 and see if the first few rows match the database factor column 
#it's the mintute cubed for the factor as the pattern