#!/usr/bin/env python
#
# Script to query local GeoIP db for a list of IP addresses to generate a
# series of latitude/longitude coordinate pairs
#
# Created 2012-12-03 by Derek Gottlieb <derek@asc.edu>

import GeoIP
import sys
import os

def print_usage():
 print "Usage: " + os.path.basename(__file__) + " ipfile.txt"

# make sure we've been passed the filename containing IP addresses
if len(sys.argv) != 2: 
 print_usage()
 sys.exit()

# grab the filename
ipfile = sys.argv[1];

# initialize the GeoIP database
gi = GeoIP.open("GeoLiteCity.dat",GeoIP.GEOIP_STANDARD)

# for each IP in the file...
for line in open(ipfile, "r"):
 # strip newlines
 ip = line.rstrip()

 # look up GeoIP record for this IP
 gir = gi.record_by_name(ip)

 # print lat/long if found in db
 if gir != None:
 	print gir['latitude'], gir['longitude']

