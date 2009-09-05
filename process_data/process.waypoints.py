# -*- coding: utf-8 -*-

"""Processes the apt - airports file"""
import sys

import yaml


from ProcessCore import ProcessCore

"""

 55.136667 -007.191389 03MCTI
600 Version - data cycle 2009.09, build 20091055, metadata FixXP700.  Copyright � 2009, Robin A. Peel (robin@xsquawkbox.net).   This data is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program ("AptNavGNULicence.txt"); if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

 22.528056 -156.170961 00MKK
 20.566668 -154.125000 00UPP
 25.610000  030.635278 03SML
 73.147778 -068.683056 04THT
 47.733334  008.283334 06TRA
 63.751277 -100.000685 08YBK
"""




class ProcessWaypoints(ProcessCore):

	def __init__(self, in_file):
		ProcessCore.__init__(self, in_file)
	
		c = 0
		data_dic = {'info': self.source_info}
		yam = {}
		js = {}
		keys = []
		data_dic['waypoints'] =[]

		
		while 1:
			line = self.read_line()
			if line == -1:
				break
			
			if line != None:
				cols = line.split()
				#temp_dic = {'lat': float(cols[0]), 'lng': float(cols[1])}
				#print json.dumps( temp_dic )
				#data_dic['waypoints'][str(cols[2])] = temp_dic
				
				
				if  DO_ALL or len(yam) < 10:
					keys.append(cols[2])
					lat = "%.6f" % float(cols[0])
					lng = "%.6f" % float(cols[1])
					yam[cols[2]] = "{waypoint: '%s', lat: %s, lng: %s}" % (cols[2], lat, lng)
					js[cols[2]] = '{"waypoint": "%s", "lat": %s, "lng": %s}' % (cols[2], lat, lng) #, cols[0],cols[1])
					#jso[cols[2]] = "{waypoint: '%s', lat: %s, lng: %s}" % (cols[2], cols[0],cols[1])
					#data_dic['waypoints'].append( {'way': cols[2],'lat': cols[0], 'lng': cols[1]} )

		self.close()
		#print len(yam)
		
		### Sort ########################
		keys_sorted = sorted(keys)
		#print keys_sorted
		yam_sort = []
		js_sort = []
		for k in keys_sorted:
			yam_sort.append( yam[k] )
			js_sort.append( js[k] )
			data_dic['waypoints'].append( k )

		#self.write_xml(data_dic, 'waypoints')
		#return

		###############################
		## Write Yaml
		yam_str = self.credits('yaml') + "\n" 
		yam_str += "waypoints:\n"
		yam_idx_str  = yam_str
		
		yam_str += '\n'.join(["- %s" % i for i in yam_sort])
		self.write_out('yaml', yam_str, 'waypoints')

		yam_idx_str += "\n".join(["- '%s'" % i for i in keys_sorted])
		self.write_out('yaml', yam_idx_str, 'waypoints.index')

		###############################
		## Write Json
		json_str = '{"info":' + self.credits('js') + ',\n'
		json_str += '"waypoints":[\n'
		json_idx_str  = json_str	
	
		json_str += ',\n'.join(["%s" % i for i in js_sort])
		
		json_str += "\n]\n}"
		self.write_out('js', json_str, 'waypoints')

		json_idx_str += ',\n'.join(['"%s"' % i for i in keys_sorted])
		json_idx_str += "\n]\n}"
		self.write_out('js', json_idx_str, 'waypoints.index')


		#{ifo 'fooo', waypoints: [ {} }
		#s += "\n"
#		s += "- %s\n" % yam[k]
		#	data_dic['waypoints'].append(yam[k])
		
		#self.write_yaml(data_dic, 'waypoints')

		print "  done"

		
DO_ALL = len(sys.argv) == 1
	

d = ProcessWaypoints("../temp/Resources/default data/earth_fix.dat")
