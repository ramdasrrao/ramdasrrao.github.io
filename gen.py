import sys
import csv
from string import Template
from datetime import datetime, timedelta

t = Template('x is $x, y is $y')

# Load event template
evtTempFile = open('ical_template2.txt')
evtTemplateString = evtTempFile.read()
evtTemplate = Template(evtTemplateString)

# print(evtTemplateString)


currYear = ''
eventsString = ''

with open(sys.argv[1], newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    stDate = datetime.strptime(row[0], '%Y%m%d')
    endDate = stDate + timedelta(1)
    desc = row[1] + " on " + stDate.strftime("%d-%b-%Y (%A)")


    currYear = stDate.year

    # print(evtTemplate.substitute(stDate = dt, endDt = desc = desc))
    # print(stDate.strftime('%Y%M%d'), endDate.strftime('%Y%M%d'), desc)

    stDateString = stDate.strftime('%Y%m%d')
    endDateString = endDate.strftime('%Y%m%d')

    # print(t.substitute(x = dt, y = desc))
    eventsString += evtTemplate.substitute(stDate = stDateString, endDate = endDateString, desc = desc)

# print(eventsString)


# Load calendar template
calTempFile = open('ical_template1.txt')
calTemplateString = calTempFile.read()
calTemplate = Template(calTemplateString)

print(calTemplate.substitute(year = currYear, events = eventsString))
