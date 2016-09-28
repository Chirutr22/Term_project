import csv
import json
import pymongo
from pymongo import MongoClient


class LoadData:
	def __init__(self):
		self._path = "/home/chiru/Term_project/countries/"
		self.infile = open(self._path + "sorted.csv","r")
		self.outfile = open(self._path + "Olympicsdata.json","w")

	def connect_database(self):
		connection=MongoClient()
		self.db=connection.Olympics
		self.collection=self.db.olympics_medal_tally

	def csvtojson(self):
		fieldnames = ("country","year","participants","male","female","sports","gold","silver","bronze","total")
		reader = csv.DictReader( self.infile, fieldnames)
		out = json.dumps( [ row for row in reader ] )
		print(out)
		self.outfile.write(out)
		self.outfile.close();

	def LoadtoMongo(self):
		jsonfile=open(self._path + "Olympicsdata.json",'r')
		jsonarray=json.loads(jsonfile.read())
		for document in jsonarray:
		   self.collection.insert(document) 
	


 