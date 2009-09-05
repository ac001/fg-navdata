# -*- coding: utf-8 -*-

"""Processes the apt - airports file"""
import sys
#import csv
import yaml
import json

in_file_name = "Resources/default data/earth_fix.dat"


"""
I
600 Version - data cycle 2009.09, build 20091055, metadata FixXP700.  Copyright � 2009, Robin A. Peel (robin@xsquawkbox.net).   This data is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program ("AptNavGNULicence.txt"); if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

 22.528056 -156.170961 00MKK
 20.566668 -154.125000 00UPP
 55.136667 -007.191389 03MCT
 25.610000  030.635278 03SML
 73.147778 -068.683056 04THT
 47.733334  008.283334 06TRA
 63.751277 -100.000685 08YBK
"""



class ProcessWaypoints:

	#col_map = {'key':0, 'elevation':1, 'atc':2, '_':3, 'icao':4, 'name':5}

	def __init__(self, in_file_name):
		self.in_file = open(in_file_name)
		

	def run(self):
		#self.airports_csv = csv.writer(open(airports_csv, 'w'), quoting=csv.QUOTE_ALL)
		
		# skip first three lines
		self.read_line()
		info = self.read_line()
		self.read_line()
		#self.read_line()

		## Loop lines to read data
		data_dic = {}
		c = 0
		while 1:
			line = self.read_line()
			#print c, line
			#print line
			if line == -1:
				break
			
			if line != None:
				cols = line.split()
				waypoint = str(cols[2])
				data_dic[waypoint] = {'waypoint': waypoint, 'lat': float(cols[0]), 'lng': float(cols[1])}

		self.close()

		yaml_file_name = "../fg_data_app/yaml/waypoints.yaml"
		json_file_name = "../fg_data_app/json/waypoints.json"
		self.yaml_file = open(yaml_file_name, 'w')
		self.json_file = open(json_file_name, 'w')

		print "writing files"
		sorted_keys = sorted(data_dic.keys())		
		c == 0
		for ki in sorted_keys:
			yaml.dump(data_dic[ki], self.yaml_file, width=500, indent=4)
			self.json_file.write( "%s\n" % json.dumps(data_dic[ki]) )

			if c % 1000 == 0:
				print c,  data_dic[ki]
			c += 1
		self.yaml_file.close()
		self.json_file.close()
		
		print "### done ####"
		

	def read_line(self):
		line =  self.in_file.readline()
		## End of file reached
		if not line:
			print "End of file "
			self.close()
			return -1
		
		line = line.strip()

		## check its not END flag = 99
		if line == '99':
			print "End of file flag reached"
			self.close()
			return -1

		## return Null if its not a text line
		if line == '':
			return None
		return line

	def close(self):
		self.in_file.close()

		

d = ProcessWaypoints(in_file_name)
d.run()