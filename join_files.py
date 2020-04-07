from glob import glob
import pymorphy2

train_path = '/home/anna/Desktop/markup/brat_data/teach_embed/valid.txt'
train_path_to = '/home/anna/Desktop/markup/brat_data/teach_embed/valid_new.txt'
morph = pymorphy2.MorphAnalyzer()

# with open(train_path, 'r') as f:
	# with open(train_path, "w") as out:
		# for line in f:
		# loc_line = f.read().split()
		# print("ll =", loc_line)
		# print(len(loc_line))
# with open(train_path_to, "w") as out:
# 	for i in loc_line:
# 		if len(i) > 0:
# 			i = morph.parse(i.lower())[0].normal_form
		# print(i)
				# loc_line = loc_line[0]+" "+loc_line[1]
			# out.write(i + " ")
			# else:
			# 	out.write("\n")
# raise Exception

filepath = glob('/home/anna/Desktop/markup/brat_data/train/*.txt')
filepath_to = '/home/anna/Desktop/markup/brat_data/teach_embed/train/train.txt'
test_data = []
for d in filepath:
	print(d)
	with open(d, "r") as f:
		test_data.append(f.read().splitlines())
raise Exception
test_data = sum(test_data, [])

with open(filepath_to, 'w') as f:
	for line in test_data:
		f.write(line)
print(test_data[:50])
