import csv

def load(csv_path):
	csv_file = csv.reader(open(csv_path, 'rb'))
	items = [item for item in csv_file][1:]
	X = []
	y = []
	for item in items:
        	X.append([float(i) for i in item[:-1]])
		y.append(item[-1])
	return X, y
