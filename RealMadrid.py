#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb

print "Content-type:text/html\r\n\r\n"



def getTeamInfo():
  response = requests.get('http://api.football-data.org/v1/teams/86/players')
  headers = { 'X-Auth-Token': '0be185032c9644beb521dd6d43400482', 'X-Response-Control': 'minified' }
  return response.json()['players']

info = getTeamInfo()

print "<table border='1' align='center'>"
print "<tr><td>Name</td><td>Position</td><td>Jersey Number</td><td>DOB</td><td>Nationality</td><td>Contract Until</td></tr>"
for row in info:
  print "<tr>"
  print "<td>"+(row['name']).encode('utf-16')[2:]+"</td>"  
  print "<td>"+str(row['position'])+"</td>"
  print "<td>"+str(row['jerseyNumber'])+"</td>"
  print "<td>"+str(row['dateOfBirth'])+"</td>"
  print "<td>"+str(row['nationality'])+"</td>"
  print "<td>"+str(row['contractUntil'])+"</td>"
 
  
  print "</tr>"
   
