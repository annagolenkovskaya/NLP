import csv

final_filepath_csv = '/home/anna/Desktop/markup/brat_data/final_annotation.csv'

data = []

with open(final_filepath_csv, newline='') as csvfile:
	rd = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in rd:
		tmp1 = row[1].split(' ')
		tmp2 = row[2]
		data.append((tmp1, tmp2))

data = data[1:]

new_data = []
for d in range(len(data)):
	if len(data[d][0]) > 1:
		i = 0
		for w in range(len(data[d][0])):
			if w > 0:
				new_data.append((data[d][0][w], "I-" + data[d][1]))
			else:
				new_data.append((data[d][0][w], "B-" + data[d][1]))

res = []
for d in new_data:
	print(d)