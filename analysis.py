import mysql.connector
import sqlite3
import requests
import json
import time
import schedule
import requests
import math


# Hypothesis: after initial glance at the table, it looks like the factor are cubes of numbers starting from 1
# Hypothesis 2: Pi gets closer to the value of actual pi as time goes on

# Connect to database to be able to read from the table that contains the API information 
mydb = mysql.connector.connect(
  host="localhost",
  user="ayushi",
  password="Ayushi29",
  database = "final_data"
)

# Make an array that is the same length as how long we called the API for, with the index as what should be cubed and stored
# in the array
cubes = [0] * 60

for i in range(60):
  if i == 0:
    cubes[0] = 1
  else:
    cubes[i] = i * i * i

mycursor = mydb.cursor()
# Select the factor column from the table and executr the query written below
select_query = """SELECT FACTOR from pi_data9"""
mycursor.execute(select_query)
# Fetch all the rows
records = mycursor.fetchall()
# Check if each row in the table matches the cube array made previously 
j = 0
for row in records:
  print(row[0] == cubes[j])
  j = j + 1

# ANALYSIS: Found that it printed true for all the elements, thus the factor is increasing cubes based on the minute it is running
# (i.e. if the API is called at time 2, the factor will be 8)

# To test hypothesis 2, make a variable called pi, and another array of 60 numbers
# For each pi row, subtract the actual value of pi from what is stored in the table and print out the array at the end
# to see if the number gets closer to 0

pi_val = math.pi
pi_array = [0] * 60
# Select the factor column from the table and executr the query written below
select_query = """SELECT PI from pi_data9"""
mycursor.execute(select_query)
# Fetch all the rows
records_two = mycursor.fetchall()
j = 0
for row in records_two:
  pi_array[j] = pi_val - row[0]
  j = j + 1

for item in pi_array:
  print(item)

# ANALYSIS: Found that the difference got closer to 0 as time went on given



