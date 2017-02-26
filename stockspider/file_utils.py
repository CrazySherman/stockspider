# Date: 2017/02/25
# Author: Sherman
# Description:
# 	there're consistency issues on using write_back, espically if there're multiple updates happening at the same time, 
# 	we should consider using database...but rly?



FILE_PATH = "stockspider/inc_list.txt"
DELIM = " "

def load_current_incs():
	res = {}
	with open(FILE_PATH) as f:
		for line in f:
			fields = line.split()
			print fields
			if len(fields) == 2:
				name, date = fields
			elif len(fields) == 1:
				name = fields[0]
				date  =  ''
			else:
				print '[Debugging]:: line corrupted...'
				continue   #corrupt line
			if not name.isalpha():
				#also corrupt
				print '[Debugging]:: line also corrupted...'
				continue
			res[name.upper()] = date	
	return res

incs = load_current_incs()


def write_back(incs):
	if type(incs) is not dict:
		print '[Debugging]:: wrong incs type provided'
		return False
	with open(FILE_PATH, 'w') as f:
		for name, date in incs.items():
			f.write(name + DELIM + date + '\n')

	print '[Info]:: file updated successfully'
	return True
