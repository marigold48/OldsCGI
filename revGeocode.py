#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print "Content-Type: text/plain;charset=utf-8"
print

import sys
import opencage
from opencage.geocoder import OpenCageGeocode
import json
import cgi, cgitb

# Create instance of FieldStorage 
data= cgi.FieldStorage()

# Get data from fields
lat = data["lat"].value
lng = data["lng"].value

#print lat
#print lng

key = '2fcab5a7b512e6cabb28f107802aa0d0'
geocoder = OpenCageGeocode(key)
results = geocoder.reverse_geocode(lat,lng)

print json.dumps(results)