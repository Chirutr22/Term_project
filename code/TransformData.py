class TransformData:

	def __init__(self):
		self._path = "/home/chiru/Term project/countries/oly$countries/"
		self.infile = open(self._path + "all.csv")
		self.outfile = open(self._path + "sorted.csv","w")
       
	def read_file(self):
   		for record in self.infile:
   			self.process_data(record)
   			self.write_file()

	def write_file(self):
		writerec = self.country+","+self.year+","+self.participants+","+self.males+","+ self.females+","+self.sports+","+self.gold+","+self.silver+","+self.bronze+","+self.total+"\n"
		if self.year == "2012" or self.year == "2008" or self.year == "2004" or self.year == "2000" or self.year == "1996":
			print(writerec)
			self.outfile.write(writerec)
   			
	def get_year(self, string):
		year = string.split(' ')
		return(year[0])

	def process_data(self,record):
		strings = record.split(',')
		self.country = strings[0]
		self.year = (self.get_year(strings[2]))
		self.participants = (strings[4])
		self.males =  (strings[5])
		self.females = (strings[6])
		self.sports = (strings[7])
		if strings[8] == "":
			self.gold = "0"
		else:
			self.gold = (strings[8])
		if strings[9] == "":
			self.silver = "0"
		else:
			self.silver = (strings[9])
		if strings[10] == "":
			self.bronze = "0"
		else:
			self.bronze = (strings[10])
		if strings[11] == "":
			self.total = "0"
		else:
			self.total = (strings[11]);
   		#print(self.country,self.year,self.gold,self.silver,self.bronze)


if __name__ == '__main__':
	data = TransformData()
	data.read_file()
