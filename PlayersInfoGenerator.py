#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb,sqlite3

conn = sqlite3.connect("Players.db")

conn.execute("Create Table Player(Name varchar(30),Club varchar(30),Nationality varchar(20),Position Varchar(20),Appearances integer,Goals integer, Assists integer,PassCompletion real,DribblesPerGame real,TacklesperGame real)")
conn.execute("Insert into Player Values('Lionel Messi','FC Barcelona','Aregntina','Forward',11,12,8,86.2,5.2,0.4)")
conn.execute("Insert into Player Values('Cristiano Ronaldo','Real Madrid','Portugal','Forward',11,1,2,84.2,1.2,0.45)")
conn.execute("Insert into Player Values('Kevin De Bryune','Manchester City','Belgium','Central Midfielder',11,2,6,83.2,1.8,1.9)")
conn.execute("Insert into Player Values('Romelu Lukaku','Manchester United','Belgium','Forward',10,7,3,85.8,0.6,0.2)")
conn.execute("Insert into Player Values('Robert Lewandowski','FC Bayern Munich','Poland','Forward',11,11,0,80.9,0.2,0.3)")

conn.commit()


