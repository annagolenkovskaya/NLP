path = '/home/anna/Desktop/markup/brat_data/new/dev.txt'
path_to = '/home/anna/Desktop/markup/brat_data/new/dev_alter.txt'
with open(path, 'r') as f:
	file = f.readlines()

tags = []
outs = []

for f in file:
	f = f.split()
	if (len(f)) > 1:
		if f[1] == 'OUT':
			outs.append(f)
		else:
			tags.append(f)
	else:
		outs.append('\n')
print(len(outs), outs[:10])
print(len(tags), tags[:10])

alter = []
l = 0

for l in range(len(tags) - 1):
	# print("l =", l)
	alter.append(tags[l])
	if len(tags) > 1 and tags[l][1][1:] != tags[l + 1][1][1:]:
		alter.append(outs[l])

print("l =", l)
for i in range(l, len(outs)):
	alter.append(outs[i])

print(alter)
print(len(alter))

c = 0
with open(path_to, 'w') as f:
	for l in alter:
		c += 1
		print(l)
		if c % 40 == 0:
			f.write('\n')
		if len(l) > 1:
			f.write(l[0])
			f.write(' ')
			f.write(l[1])
			f.write('\n')
		else:
			f.write('\n')