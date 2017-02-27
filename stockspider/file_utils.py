# Date: 2017/02/25
# Author: Sherman
# Description:
# 	there're consistency issues on using write_back, espically if there're multiple updates happening at the same time, 
# 	we should consider using database...but rly?

import json

FILE_PATH = "stockspider/inc_list.txt"
DELIM = " "

def load_current_incs():
	res = {}
	with open(FILE_PATH) as f:
		objs = json.load(f)
		for elem in objs:
			res[elem["name"]] = elem["date"]
	# print res
	return res


def write_back(incs):
	if type(incs) is not dict:
		print '[Debugging]:: wrong incs type provided'
		return False
	with open(FILE_PATH, 'w') as f:
		objs = []
		for name, date in incs.items():
			objs.append({"name": name, "date": date})
		jsonstr = json.dump(objs, f, indent = 4)

	print '[Info]:: file updated successfully'
	return True
