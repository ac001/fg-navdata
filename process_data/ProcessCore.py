# -*- coding: utf-8 -*-

import yaml
import json
import xml.etree.ElementTree as ElementTree


class ProcessCore:

	def __init__(self, in_file):
		
		self.in_file = open(in_file)
		print "Reading source: %s" % in_file

		self.data_dic = {}

		# skip first
		self.read_line()

		# read info line
	
		src_info = self.read_line()
		self.source_info = ''
		
		for s in src_info:
			if ord(s) != 169: ## get rid of strange copy
				self.source_info += s
			#c += 1
			#if c == 90: 
			#	break
		
	def to_yaml(self, data_dic):
		return yaml.dump( data_dic, width=1000, indent=2 )

	def credits(self, typ):
		if typ == 'yaml':
			return "info: %s" % self.source_info
		elif typ == 'js':
			return json.dumps( self.source_info)
	

	def write_yaml(self, data_dic, file_part):
		print " > writing yaml"
		file_name = "../fg_data_app/yaml/%s.yaml" % file_part
		fileObj = open(file_name, 'w')
		yaml.dump(data_dic, fileObj, width=1000, indent=4)
		fileObj.close()

	def write_json(self, data_dic, file_part):
		print " > writing json"
		file_name = "../fg_data_app/json/%s.json" % file_part
		fileObj = open(file_name, 'w')
		json.dump(data_dic, fileObj, indent=0)
		fileObj.close()

	def write_xml(self, data_dic, file_part):
		print " > writing xml"
		file_name = "../fg_data_app/xml/%s.xml" % file_part
		fileObj = open(file_name, 'w')
		json.dump(self.to_xml(data_dic), fileObj, indent=0)
		fileObj.close()

	def to_xml(self, dic):
		print dic
		elem = ElementTree.Element("root")
		for key, value in dict.items():
			if isinstance(value, type(0)):
				ElementTree.SubElement(elem, key, type="int").text = str(value)
			else:
				ElementTree.SubElement(elem, key).text = value
		return ElementTree.tostring(elem)


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
		#return line
		#print "------------"
		#un = unicode(line, 'latin-1')
		return line


	def close(self):
		self.in_file.close()

	def write_out(self, enc_type, string, file_part):
		file_name = "../fg_data_app/%s/%s.%s" % (enc_type, file_part, enc_type)
		print "> writing ", file_name
		f = open(file_name, 'w')
		f.write( string + "\n" )
		f.close()
		print "  done"