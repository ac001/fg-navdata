# -*- coding: utf-8 -*-

"""Processes the apt - airports file"""
import sys
import csv
import yaml

in_file_name = "../temp/Resources/default scenery/default apt dat/Earth nav data/apt.dat"
airports_csv = "../prepared_data/airports.csv"
airports_yaml = "../fg_data_app/yaml/airports.yaml"

"""
class Airport(db.Model):
	icao = db.StringProperty()
	name = db.StringProperty()
	heliport = db.BooleanProperty()
	seaport = db.BooleanProperty()
	elevation = db.IntegerProperty()
	atc = db.BooleanProperty()
"""


class ProcessAirports:

	col_map = {'key':0, 'elevation':1, 'atc':2, '_':3, 'icao':4, 'name':5}

	def __init__(self, in_file_name, airports_csv, airports_yaml):
		self.in_file = open(in_file_name)

		#self.airports_csv = csv.writer(open(airports_csv, 'w'), quoting=csv.QUOTE_ALL)
		self.airports_yaml = open(airports_yaml, 'w')
		# skip first three lines
		self.read_line()
		self.read_line()
		self.read_line()

		airports = {}
		c = 0
		while 1:
			line = self.read_line()
			#print c, line
			#print line
			if line != '':
				cols = line.split()
				## aiport, seaplane, heliport
				akey = cols[0]
				
				heliports = []
				seaports = []
				if akey != '99':
					if akey in ['1', '16', '17']:
						seaport = True if akey == '16' else False
						heliport = True if akey == '17' else False
						#                            icoa,    name,    seaport, heliport, elev,    atc
						#print cols
						airport = " ".join(cols[5:])
						icao = str(cols[4])
						#self.airports_csv.writerow( [cols[4], airport, seaport, heliport, cols[1], cols[2]] )
						airports[icao] = { 
								'name': str(airport), 
								'seaport': seaport, 
								'heliport': heliport,
								'elevation': int(cols[1]),
								'atc': bool(cols[2])
						}
						
						#yaml.dump(yam, self.airports_yaml, width=500, indent=4)
						if c % 100 == 0:
							print c, cols[4], airport
						if c == 1000:
							print "break"
							break
						c += 1
		sorted_airports = sorted(airports.keys())
		print sorted_airports
		for ki in sorted_airports:
			data = {ki: airports[ki]}
			yaml.dump(data, self.airports_yaml, width=500, indent=4)
		print "### done ####"
		self.close()

	def read_line(self):
		line =  self.in_file.readline()
		if not line:
			print "End of file flag reached"
			self.close()
		return line.strip()

	def close(self):
		self.in_file.close()

		

d = ProcessFile(in_file_name, airports_csv, airports_yaml)
