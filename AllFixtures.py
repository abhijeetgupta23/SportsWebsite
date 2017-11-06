#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb

print "Content-type:text/html\r\n\r\n"

#EPLKey = "445"

def getRecentFixtures():
  response = requests.get('http://api.football-data.org/v1/fixtures')
  headers = { 'X-Auth-Token': '80b631eb05404f328176874d6a7d2452', 'X-Response-Control': 'minified' }
  return response.json()['fixtures']

results=getRecentFixtures()

print "<html>"
print "<body>"

print "<table border='1' align='center'>"
print "<tr><td>Status</td><td>Date</td><td>Home Team</td><td colspan='2'>Score</td><td>Away Team</td></tr>"
for row in results:
  print "<tr>"
  print "<td>"+(str(row['status']))+"</td>"  
  print "<td>"+str(row['date'])+"</td>"
  print "<td>"+row['homeTeamName'].encode('utf-16')[2:]+"</td>"
  
  print "<td>"+str(row['result']['goalsHomeTeam'])+"</td>"
  print "<td>"+str(row['result']['goalsAwayTeam'])+"</td>"
  print "<td>"+row['awayTeamName'].encode('utf-16')[2:]+"</td>"
  
  print "</tr>"

print "</table>"
print "</body>"
print "</html>"
  
