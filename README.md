# DS3002-final-project

# Documentation 


### Process 
The process that I took for this project is splitting up the project into benchmarks. The first was to successfully call the API and retrieve the information. I did this using requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi") where the link is the API that we were provided. I also converted this to JSON using response.json() to ensure that I could retrieve all fields of the API correctly. 

After this, I researched how to run functions in python for a set amount of time since one of the tasks for this project was to execute the solution precisely once per minute. I found the schedule library which had a function called schedule.every(x).minutes.do(job). This would allow me to run a function every x minutes, so I supplied 1 for the argument. Our solution has to run for exactly one hour, and the schedule library also supplies an argument .until(timedelta(minutes=x)) where x specifies how many minutes you want to run the code for. Thus, I added the line schedule.every(1).minutes.until(timedelta(minutes=59)).do(job) to my code to run the job function every minute for an hour. The job function is where the API gets called and stored in the database, so the next step that I focused on was connecting to a mysql database and inserting the API information into the database.

The database that I chose to connect to was MySql. I used [this](https://www.w3schools.com/python/python_mysql_getstarted.asp) link to understand what code I needed to have to connect to a database. I added this to my file, which connects to the specific instance defined by the username, password, and database:

mydb = mysql.connector.connect(
  host="localhost",
  user="ayushi",
  password="xxxxxxxx",
  database = "final_data"
)

I ran into an error (ERROR 1045 (28000): Access denied for user 'ayushi'@'localhost' (using password: YES)) and [this] (https://stackoverflow.com/questions/10299148/mysql-error-1045-28000-access-denied-for-user-billlocalhost-using-passw) helped me understand that I have to create ayushi@localhost and grant priveleges to that account. On MySQL workbench, I pasted this code:

CREATE USER ayushi@localhost IDENTIFIED BY 'Ayushi29';
grant all privileges on *.* to ayushi@localhost with grant option;

and was successfully able to connect to the database. From there, I was able to execute SQL queries to insert the API information to a precreated table in the database. 

### Code
There are two python files - test.py and analysis.py. Test.py contains the code that does all of the above mentioned procedures. There are comments detailing what each of the lines do. The analysis.py file is used to affirm the trend in the data.

### Deployment Strategy
To run this code, type in python3 test.py or python3 analysis.py. This will start the execution of the file, including connecting to MySQL where the data is deployed to. Change the username, password, and database fields if you would like to export the data to your own table, where you can then export the final data to a csv to analyze the trends. 
