import pymorphy2

train_path = '/home/anna/Desktop/markup/brat_data/all_altered/test_alter.txt'
morph = pymorphy2.MorphAnalyzer()

with open(train_path, 'r') as f:
	with open(train_path+"_morph.txt", "w") as out:
		for line in f:
			loc_line = line.split()
			if len(loc_line) > 1:
				print(loc_line)
				loc_line[0] = morph.parse(loc_line[0].lower())[0].normal_form
				loc_line = loc_line[0]+" "+loc_line[1]
				out.write(loc_line+"\n")
			else:
				out.write("\n")
