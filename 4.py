"""На основе заданий 2-3, посчитать файлы, аналогичные заданию 2, для словосочетаний типа:
первое слово - прилагательное, второе - существительное
первое слово - отрицание, второе - глагол
первое слово - отрицание, второе - существительное
первое слово - отрицание, второе - прилагательное
Оставить только те словосочетания, где одно из двух слов входит в один из словарей.
Результаты отсортировать по убыванию частоты и записать в csv файлы (аргумент скрипта),
 формат: словосочетание, шаблон (), тональность (по одному из слов), источник (linis or rusentilex), частота.
 1 строка каждого файла должна быть header: MWE, pattern, sentiment, resource, frequency
Шаблон задается вида {}_{}.format(tag1,tag2), где tag1 - часть речи 1го слова, tag2 - второго слова. Например, ADJ_NOUN
1) улучшить код, 2) найти все словосочетания, где одно из 2 слов из словаря, создать новую таблицу."""

from utils import read_reviews, read_rusentilex_pos, read_linis_pos
import re,csv, argparse
from task3 import bigrams, dict_pos
from collections import Counter

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('rusentilex', type=str, help='path to rusentilex file')
	parser.add_argument('linis', type=str, help='path to linis file')
	parser.add_argument('reviews', type=str, help='path to reviews file')
	parser.add_argument('csv_path', type=str, help='path where to write csv file')
	args = parser.parse_args()
	rusentilex_path = args.rusentilex
	linis_path = args.linis
	reviews_path = args.reviews
	path = args.csv_path

	# rusentilex_path = '/home/anna/Desktop/rusentilex_pos.txt'
	# linis_path = '/home/anna/Desktop/linis_pos.txt'
	# reviews_path = '/home/anna/Desktop/otzovik_medicine.json'
	# path = '/home/anna/Desktop/neg_noun.csv'
	rusentilex = read_rusentilex_pos(rusentilex_path)
	linis = read_linis_pos(linis_path)
	reviews = read_reviews(reviews_path)[:800]
	print(len(reviews))
	print("a")
	for r in range(len(reviews)):
		reviews[r] = re.sub("[^\w]", " ", reviews[r]).split()

	print("b")

	adj_noun = bigrams(reviews, adj_noun=False, neg_verb=False, neg_noun=True, neg_adj=False)[1]
	print("c")
	found = []
	tones = []
	for review in adj_noun:
		for bigram in review:
			for line in rusentilex:
				if bigram[0] == line[0]:
					tone = [bigram[0], line[1], 'rusentilex']
					found.append(bigram[0])
					tones.append(tone)
				print("aa", len(tones))

				if bigram[1] == line[0]:
					tone = [bigram[1], line[1], 'rusentilex']
					found.append(bigram[1])
					tones.append(tone)
			print("bb", len(tones))

			if bigram[0] not in found:
				for line in linis:
					if bigram[0] == line[0]:
						tone = [bigram[0], line[1], 'linis']
						found.append(bigram[0])
						tones.append(tone)
			print("cc", len(tones))
			if bigram[1] not in found:
				for line in linis:
					if bigram[1] == line[0]:
						tone = [bigram[1], line[1], 'linis']
						found.append(bigram[1])
						tones.append(tone)
	print("d")

	unique_bigrams = []
	for review in adj_noun:
		for bigram in review:
			for word in tones:
				if bigram[0] == word[0] or bigram[1] == word[0]:
					unique_bigrams.append(bigram[0] + ' ' + bigram[1] + ', ' + word[1] + ', ' + word[2])
	print("e")

	for word in range(len(unique_bigrams) -1 , -1, -1):
		if 'neutral' in unique_bigrams[word]:
			del unique_bigrams[word]
	print("f")

	copy = unique_bigrams.copy()
	for b in range(len(copy)):
		copy[b] = re.sub("[^\w]", " ", copy[b]).split()
	print("g")

	counter = Counter(unique_bigrams)
	print("h")

	keys = []
	for  i in counter.keys():
		keys.append(i)
	print("i")

	values = []
	for v in counter.values():
		values.append(v)
	print("j")

	for  k in range(len(keys)):
		keys[k] = re.sub("[^\w]", " ", keys[k]).split()
	print("k")

	mwe = []
	pattern = []

	for k in keys:
		mwe.append(k[0][:k[0].find("_")] + ' ' + k[1][:k[1].find("_")])
		pattern.append(k[0][k[0].find("_") + 1:] + k[1][k[1].find("_"):])
	print("l")

	to_write = []
	for i in range(len(mwe)):
		to_write.append(mwe[i] + ', ' + pattern[i] + ', ' + keys[i][2] + ', ' + keys[i][3] + ', ' + str(values[i]))
	print("m")

	for w in range(len(to_write)):
		to_write[w] = re.sub("[^\w]", " ", to_write[w]).split()
	print("n")

	to_write = sorted(to_write, key=lambda  w: int(w[5]), reverse=True)
	string = 'MWE, pattern, sentiment,resource, frequency'
	string = re.sub("[^\w]", " ", string).split()
	to_write.insert(0, string)
	print("o")

	for w in range(len(to_write)):
		to_write[w][0] = to_write[w][0] + ' ' + to_write[w][1]
	print("p")

	for i in range(len(to_write)):
		for j in range(1, len(to_write[i]) - 1):
			to_write[i][j] = to_write[i][j + 1]
		del to_write[i][-1]
	print("q")

	with open(path, "w", newline="") as f:
		cw = csv.writer(f)
		cw.writerows(r for r in to_write)
