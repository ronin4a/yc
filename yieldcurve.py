import csv
import requests
import xml.etree.ElementTree as ET
import pandas

_XML_FILE_NAME = 'yieldcurve.xml'

#TODO: handle exceptions for http responses
def loadxml_from_site():
  """Load xml from a url."""
  url = "http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%206%20and%20year(NEW_DATE)%20eq%202018"
  resp = requests.get(url)
  with open(_XML_FILE_NAME,'wb') as data:
    data.write(resp.content)

#TODO: parse xml file
def parse_xml(xmlfile):
  tree = ET.parse(xmlfile)

  root = tree.getroot()

  print(root)

#TODO use pandas to graph yield curve and its changes over the last N time
# periods
def graph_curve(_DATATYPE_HERE):
  return

def main():
  loadxml_from_site()
  parse_xml(_XML_FILE_NAME)

if __name__=="__main__":
  main()
