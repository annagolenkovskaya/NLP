from glob import glob
from collections import Counter

data = glob('/home/anna/Desktop/markup/brat_data/train_part_1/*.ann')
fils = []
for d in data:
	with open(d, "r") as fil:
		fils.append(fil.read().split())

# for d in fils:
# 	print(d)

met = 0
eco = 0
bin = 0
cmp = 0
qua = 0
act = 0
inst = 0
soc = 0

nng = 0
nnt = 0
nps = 0
png = 0
pnt = 0
pps = 0
fng = 0
fnt = 0
fps = 0
gol = 0
tsk = 0

wordsmet = []
wordseco = []
wordsbin = []
wordscmp = []
wordsqua = []
wordsact = []
wordsinst = []
wordssoc = []

for f in fils:
	for w in range(len(f)):
		if f[w] == 'MET':
			met += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordsmet.append(tmp)
		elif f[w] == 'ECO':
			eco += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordseco.append(tmp)
		elif f[w] == 'BIN':
			bin += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordsbin.append(tmp)
		elif f[w] == 'CMP':
			cmp += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordscmp.append(tmp)
		elif f[w] == 'QUA':
			qua += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordsqua.append(tmp)
		elif f[w] == 'ACT':
			act += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordsact.append(tmp)
		elif f[w] == 'INST':
			inst += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordsinst.append(tmp)
		elif f[w] == 'SOC':
			soc += 1
			i = 3
			tmp = []
			while w + i < len(f) and f[w + i][0] != 'T':
				tmp.append(f[w + i])
				i += 1
			wordssoc.append(tmp)
		elif f[w] == 'NNG':
			nng += 1
		elif f[w] == 'NNT':
			nnt += 1
		elif f[w] == 'NPS':
			nps += 1
		elif f[w] == 'PNG':
			png += 1
		elif f[w] == 'PNT':
			pnt += 1
		elif f[w] == 'PPS':
			pps += 1
		elif f[w] == 'FNG':
			fng += 1
		elif f[w] == 'FNT':
			fnt += 1
		elif f[w] == 'FPS':
			fps += 1
		elif f[w] == 'GOL':
			gol += 1
		elif f[w] == 'TSK':
			tsk += 1

print(nng)
print(nnt)
print(nps)
print(png)
print(pnt)
print(pps)
print(fng)
print(fnt)
print(fps)
print(gol)
print(tsk)
 
# for l in range(len(wordsmet)):
# 	wordsmet[l] = ' '.join(wordsmet[l])
# print(wordsmet)
#
# for l in range(len(wordseco)):
# 	wordseco[l] = ' '.join(wordseco[l])
# print(wordseco)
# for l in range(len(wordsbin)):
# 	wordsbin[l] = ' '.join(wordsbin[l])
# print(wordsbin)
# for l in range(len(wordscmp)):
# 	wordscmp[l] = ' '.join(wordscmp[l])
# print(wordscmp)
# for l in range(len(wordsqua)):
# 	wordsqua[l] = ' '.join(wordsqua[l])
# print(wordsqua)
# for l in range(len(wordsact)):
# 	wordsact[l] = ' '.join(wordsact[l])
# print(wordsact)
# for l in range(len(wordsinst)):
# 	wordsinst[l] = ' '.join(wordsinst[l])
# print(wordsinst)
# for l in range(len(wordssoc)):
# 	wordssoc[l] = ' '.join(wordssoc[l])
# print(wordssoc)

# countermet = Counter(wordsmet).most_common(10)
# countereco = Counter(wordseco).most_common(10)
# counterbin = Counter(wordsbin).most_common(11)
# countercmp = Counter(wordscmp).most_common(11)
# counterqua = Counter(wordsqua).most_common(10)
# counteract = Counter(wordsact).most_common(10)
# counterinst = Counter(wordsinst).most_common(10)
# countersoc = Counter(wordssoc).most_common(10)

# fils = sum(fils, [])

# print(countermet)
# print(countereco)
# print(counterbin)
# print(countercmp)
# print(counterqua)
# print(counteract)
# print(counterinst)
# print(countersoc)


