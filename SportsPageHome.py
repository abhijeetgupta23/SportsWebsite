#!C:\Python27\python.exe

import requests
import json
import cgi,cgitb

print "Content-type:text/html\r\n\r\n"

def getLatestNews():
  response = requests.get('https://newsapi.org/v1/articles?source=four-four-two&sortBy=latest&apiKey=53ba432f19694b2f98927a2e93c7d34d')
  return (response.json())['articles']



news = getLatestNews()
#print news
print "<html>"
print "<body>"

print "<table border='1' cellpadding='50px'>"
print "<tr>"
print "<td><p class='menu'><a href='http://localhost/cgi-bin/LeagueTables.py' target='_blank'>League Tables</a></p></td>"
print "<td><p class='menu'><a href='http://localhost/cgi-bin/AllFixtures.py' target='_blank'>Fixtures</a></p></td>"
print "<td><p class='menu'><p>Teams</p><ul><li><a href='http://localhost/cgi-bin/FCBarcelona.py' target='_blank'>FC Barcelona</li><li><a href='http://localhost/cgi-bin/RealMadrid.py' target='_blank'>Real Madrid</li><li><a href='http://localhost/cgi-bin/ManchesterCity.py' target='_blank'>Manchester City</a></li><li><a href='http://localhost/cgi-bin/ManchesterUnited.py' target='_blank'>Manchester United</li><li><a href='http://localhost/cgi-bin/FCBayern.py' target='_blank'>FC Bayern Munich</li></ul></a></p></td>"
print "<td><p class='menu'><a href='http://localhost/cgi-bin/PlayersInfo.py' target='_blank'>Players</a></p></td>"
print "</tr>"
print "</table>"

for row in news:
  
  print "<h2>"+str(row["title"])+"</h2><br>"
  print "<img src='"+str(row['urlToImage'])+"'</img><br>"
  
  print "<p>"+str(row['description'])+"</p><br>"
  print "<h5><a href='"+str(row['url'])+"' target='_blank'>Read More</a></h5><br>"
  print "<br><hr>"


print "</body>"
print "</html>"
