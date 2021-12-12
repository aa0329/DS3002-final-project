import mysql.connector
import sqlite3
import requests
import json
import time
import schedule
import requests

# make an array that is powers of i^3 and see if the first few rows match the database factor column 
#it's the mintute cubed for the factor as the pattern

mydb = mysql.connector.connect(
  host="localhost",
  user="ayushi",
  password="Ayushi29",
  database = "final_data"
)

cubes = [0] * 60

for i in range(60):
  if i == 0:
    cubes[0] = 1
  else:
    cubes[i] = i * i * i

mycursor = mydb.cursor()

select_query = """SELECT FACTOR from pi_data8"""
mycursor.execute(select_query)
records = mycursor.fetchall()
j = 0
for row in records:
  print(row[0] == cubes[j])
  j = j + 1