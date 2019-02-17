# Combine the files split to comply with GitHub limits to their original sizes
def combine(filename,parts):
	with open(filename + ".csv", 'w', encoding="utf8") as outfile:
		for i in range(1,parts+1):
			fname = filename + '_' + str(i) + '.csv'
			with open(fname, encoding="utf8") as infile:
				outfile.write(infile.read())
