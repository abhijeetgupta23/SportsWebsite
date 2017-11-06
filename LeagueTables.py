#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb

print "Content-type:text/html\r\n\r\n"

EPLKey = "445"
LaLigaKey="455"
SerieAKey="456"
BundesligaKey="452"

def getTable(key):
  response = requests.get('https://api.football-data.org/v1/competitions/'+key+"/leagueTable")
  headers = { 'X-Auth-Token': '80b631eb05404f328176874d6a7d2452', 'X-Response-Control': 'minified' }
  return response.json()



print "<html>"
print "<body>"


def printTable(key):
  Table = getTable(key)['standing']
  print "<table border='1' align='center'>"
  print "<tr><td>Position</td><td>Logo</img><td>Team</td><td>Matches</td><td>Points</td><td>Goal Difference</td><td>Wins</td><td>Draws</td><td>Losses</td></tr>"
  for row in Table:
    print "<tr>"
    print "<td>"+str(row['position'])+"</td>"
    print "<td><img style='display:block;' width='40px' height='40px' src='"+(row['crestURI'].encode('utf-16')[2:] if (row['crestURI']!=None) else "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=")+"'</img></td>"
    print "<td>"+row['teamName'].encode('utf-16')[2:]+"</td>"
    print "<td>"+str(row['playedGames'])+"</td>"
    print "<td>"+str(row['points'])+"</td>"
    print "<td>"+str(row['goalDifference'])+"</td>"
    print "<td>"+str(row['wins'])+"</td>"
    print "<td>"+str(row['draws'])+"</td>"
    print "<td>"+str(row['losses'])+"</td>"
    print "</tr>"
    

print "<h2>EPL Table</h2>"
printTable(EPLKey)
print "</table><br>"

print "<h2>La Liga Table</h2>"
printTable(LaLigaKey)
print "</table><br>"

print "<h2>Serie A Table</h2>"
printTable(SerieAKey)
print "</table><br>"

print "<h2>Bundesliga Table</h2>"
printTable(BundesligaKey)
print "</table><br>"



print "</body>"
print "</html>"
  
