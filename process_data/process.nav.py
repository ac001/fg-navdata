# -*- coding: utf-8 -*-

import yaml

from ProcessCore import ProcessCore


class ProcessNav(ProcessCore):

	def __init__(self, in_file):
		ProcessCore.__init__(self, in_file)

		data_dic = {}
		data_dic['info'] =  self.file_info

		ndb = []
		vor = []
		loc = []
		loc_str = yaml.dump( data_dic, width=1000, indent=2 )
		#loc_str += "nav:\n"
		#loc_str += "  LOC:\n"
		glideslope = []
		
		data_dic['nav'] = {}
		while 1:
			line = self.read_line()
			if line == -1:
				break
			
			if line != None:
				cols = line.split()
				row_code = int(cols[0])

				#($type, $lat, $lng, $abslng, $elevation, $freq, $channelfreq, $range, $multi, '$ident', '$name', '$type_name');
				#0  1           2                  3     4   5     6   7    8
				#2  38.08783333 -077.32500000      0   396  50    0.0 APH  A P HILL NDB
				dic = {'lat': float(cols[1]), 'lng': float(cols[2])}

				## ndb
				if row_code == 2:
					
					dic['freq'] = int(cols[4])
					dic['range'] = int(cols[5])
					
					dic['ident'] = str(cols[7])
					dic['name'] = str(cols[8])
					ndb.append(dic)

				#0  1           2                  3     4   5     6   7    8
				#3  37.34752778 -075.99766667     10 11220  40  -10.0 CCV  CAPE CHARLES VORTAC
				elif row_code == 3:
					dic['elevation'] = int(cols[3])
					dic['freq'] = int(cols[4])
					dic['range'] = int(cols[5])
					dic['variation'] = float(cols[6])
					dic['ident'] = str(cols[7])
					dic['name'] = str(" ".join(cols[8:-1]))
					dic['type'] = str(cols[-1])
					vor.append(dic)

				## localiser

				elif row_code == 4 or row_code == 5:
					dic['elevation'] = int(cols[3])
					dic['freq'] = int(cols[4])
					dic['range'] = int(cols[5])
					dic['degrees'] = repr(cols[6])
					dic['ident'] = str(cols[7])
					dic['icao'] = str(cols[8])
					dic['runway'] = str(cols[9])
					dic['type'] = str(" ".join(cols[10:]))
					if len(loc) < 10:
						typ = " ".join(cols[10:])
						vs = (cols[7],   cols[8],  cols[1], cols[2], cols[4], cols[5],     cols[9], typ)
						loc.append( "- {ident: '%s', icao: '%s', lat: %s, lng: %s, freq: %s, range: %s, runway: '%s', type: '%s'}" % vs )
					#loc.append(dic)

				elif row_code == 6:
					dic['elevation'] = int(cols[3])
					dic['freq'] = int(cols[4])
					dic['range'] = int(cols[5])
					dic['degrees'] = float(cols[6])
					dic['ident'] = str(cols[7])
					dic['icao'] = str(cols[8])
					dic['runway'] = str(cols[9])
					dic['type'] = str(" ".join(cols[10:]))
					#loc.append(dic)

				else:
					break

		self.write_out('yaml', loc_str, 'nav.loc')
		return
		data_dic['nav']['LOC'] = loc
		self.write_yaml(data_dic, 'nav')

				#dic['freq'] = int(cols[4])
				#dic['chann
				
				
				#temp_dic = {'lat': float(cols[0]), 'lng': float(cols[1])}
				#print json.dumps( temp_dic )
				#data_dic['nav'][str(cols[2])] = temp_dic

		self.close()
		

d = ProcessNav('../temp/Resources/default data/earth_nav.dat')

