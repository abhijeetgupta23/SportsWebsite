#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb,sqlite3

print "Content-type:text/html\r\n\r\n"

conn = sqlite3.connect("Players.db")

print "<html>"
print "<body>"

cursor = conn.execute("Select * from player")

print "<table border='1' align='center'>"
print "<tr><td>Name</td><td>Club</td><td>Nationality</td><td>Position</td><td>Appearances</td><td>Goals</td><td>Assists</td><td>Pass Completion</td> <td>Dribbles Per Game</td><td>Tackles Per Game</td></tr>"
for row in cursor:

  print "<tr>"
  for cell in row:
    print "<td>"+str(cell)+"</td>"  
      
  print "</tr>"

print "</table>"
print "</body>"
print "</html>"
    
    
