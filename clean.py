path = '/home/anna/Desktop/markup/brat_data/marked/train/marked_train_new_all_altered_with_out.txt'
new_path = '/home/anna/Desktop/markup/brat_data/marked/train/marked_train_new_all_altered_with_out_clean.txt'
data = []
with open(path, 'r') as f:
	data = f.readlines()

print(len(data), data)
new_data = []
for d in range(len(data)):
	# print(data[d])
	if data[d][:3] == 'OUT' or data[d][2:5] == 'MET' or data[d][2:5] == 'ECO' or data[d][2:5] == 'BIN' or data[d][2:5] == 'CMP' or data[d][2:5] == 'QUA' or data[d][2:5] == 'ACT' or data[d][2:5] == 'SOC' or data[d][2:6] == 'INST':
		continue
	else:
		new_data.append(data[d])
print(len(new_data), new_data)

with open(new_path, 'w') as f:
	f.writelines(new_data)