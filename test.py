import mysql.connector
import sqlite3
import requests
import json
import time
import schedule
import requests
from datetime import datetime, timedelta

# Supply mysql database information so that we can use mysql.connector to connect to it
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

    # call the API using .get()
    response = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")

    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
      # if there is no exception, then translate the API result into JSON 
      remote_json = response.json()

    # create a sql statement to insert the API data into the database 
    sql = "INSERT INTO pi_data10 (FACTOR, PI, TIMESTAMP) VALUES (%s, %s, %s)"
    val = (remote_json["factor"], remote_json["pi"], remote_json["time"])
    # execute the sql statement by inserting the correct values into the table
    mycursor.execute(sql, val)
    # commit changes to the database 
    mydb.commit()

# use the schedule library to run this function every minute for 60 (0-59) minutes 
schedule.every(1).minutes.until(timedelta(minutes=61)).do(job)

while True:
    schedule.run_pending()
    # time.sleep(1)