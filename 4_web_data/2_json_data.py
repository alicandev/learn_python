import urllib.request
from ssl import SSLContext
import json

def printResults(data):
  # load the string data into a dictionary
  jsonData = json.loads(data)

  # access the contents of the json
  if 'title' in jsonData["metadata"]:
    print(jsonData["metadata"]["title"])

  # output the number of events and magnitude thereof
  count = jsonData["metadata"]["count"]
  print(f"{count} events recorded")

  # for each event, print the place where it occured
  for i in jsonData["features"]:
    print(i["properties"]["place"])

  # print only the events that have a magnitude of 4 or higher
  for i in jsonData["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

  # print only the events that at least 1 person reported as "felt"
  print("events that are felt:")
  for i in jsonData["features"]:
    feltReports = i["properties"]["felt"]
    if feltReports != None:
      if feltReports > 0:
        print(
          "%2.1f" % i["properties"]["mag"],
          i["properties"]["place"],
          f"reported {feltReports} times")
  
  print("--------\n")
  
# open aurl connection and read result
url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
webUrl = urllib.request.urlopen(url, context=SSLContext())
print(f"result code: {webUrl.getcode()}")
if webUrl.getcode() == 200:
  data = webUrl.read()
  printResults(data)
else:
  print("received error, cannot parse results")
