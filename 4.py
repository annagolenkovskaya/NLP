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
import re, csv, argparse, codecs, json
from task3 import bigrams
from collections import Counter


def split_by_words(file):
	# splitting the file by words
	for r in range(len(file)):
		file[r] = re.sub("[^\w]", " ", file[r]).split()
	return file


def find_in_dict(bigrams_for_work, rusentilex, linis):
	# finding the bigrams' words in the dictionaries
	found = []
	tones = []
	# cycle by reviews (all found bigrams are kept like they were in reviews)
	for review in bigrams_for_work:
		# cycle by bigrams in review
		for bigram in review:
			# cycle in rusentilex dict
			for line in rusentilex:
				# finding the first word from bigram in dict
				if bigram[0] == line[0]:
					if line[1] == 'positive' or line[1] == 'negative':
						# if found -- write the word, tonality and dict
						tone = [bigram[0], line[1], 'rusentilex']
						# write that the word was found
						found.append(bigram[0])
						tones.append(tone)

				# finding the second word of bigram in the dict
				if bigram[1] == line[0]:
					if line[1] == 'positive' or line[1] == 'negative':
						tone = [bigram[1], line[1], 'rusentilex']
						found.append(bigram[1])
						tones.append(tone)

			# if the word wasn't found
			if bigram[0] not in found:
				# look for it in linis dict
				for line in linis:
					if bigram[0] == line[0]:
						if line[1] == 'positive' or line[1] == 'negative':
							tone = [bigram[0], line[1], 'linis']
							found.append(bigram[0])
							tones.append(tone)

			if bigram[1] not in found:
				for line in linis:
					if bigram[1] == line[0]:
						if line[1] == 'positive' or line[1] == 'negative':
							tone = [bigram[1], line[1], 'linis']
							found.append(bigram[1])
							tones.append(tone)
	return tones


def unique_bigrams(bigrams_for_work, tones):
	unique_bigrams = []
	for review in bigrams_for_work:
		for bigram in review:
			for word in tones:
				# if at least one word from the bigram is in the 'found' list
				if bigram[0] == word[0] or bigram[1] == word[0]:
					# create the string from the bigram, tonality and dict
					unique_bigrams.append(bigram[0] + ' ' + bigram[1] + ', ' + word[1] + ', ' + word[2])
		# for b in unique_bigrams:
		# 	print("b =", type(b), len(b), b)

		for b in range(len(unique_bigrams)):
			unique_bigrams[b] = re.sub("[^\w]", " ", unique_bigrams[b]).split()

		for b in range(len(unique_bigrams)):
			for line in rusentilex:
				if unique_bigrams[b][0] == line[0]:
					for line in rusentilex:
						if unique_bigrams[b][1] == line[0]:
							unique_bigrams[b].append('False')
			for line in rusentilex:
				if unique_bigrams[b][0] == line[0]:
					for line in linis:
						if unique_bigrams[b][1] == line[0]:
							unique_bigrams[b].append('False')
			for line in linis:
				if unique_bigrams[b][0] == line[0]:
					for line in linis:
						if unique_bigrams[b][1] == line[0]:
							unique_bigrams[b].append('False')

	for b in range(len(unique_bigrams)- 1, -1, -1):
		if 'False' in unique_bigrams[b]:
			del unique_bigrams[b]

	return unique_bigrams


def create_file_and_write_to_csv(counter, path):
	print("c")
	# create the list from the keys of the counter dict (keys are bigrams, tonalities and dicts)
	keys = []
	for  i in counter.keys():
		keys.append(i)

	# values are the frequencies
	values = []
	for v in counter.values():
		values.append(v)
	print("j")

	# split the keys by the words
	for  k in range(len(keys)):
		keys[k] = re.sub("[^\w]", " ", keys[k]).split()

	mwe = []
	pattern = []

	for k in keys:
		# finding mwe and pattern in bigram('word1_pattern', 'word2_pattern')
		mwe.append(k[0][:k[0].find("_")] + ' ' + k[1][:k[1].find("_")])
		pattern.append(k[0][k[0].find("_") + 1:] + k[1][k[1].find("_"):])

	# create the strings that will be written in csv file
	to_write = []
	for i in range(len(mwe)):
		# 'mwe, pattern, tonality,dict, frequency'
		to_write.append(mwe[i] + ', ' + pattern[i] + ', ' + keys[i][2] + ', ' + keys[i][3] + ', ' + str(values[i]))

	# split the newly created strings by the words
	for w in range(len(to_write)):
		to_write[w] = re.sub("[^\w]", " ", to_write[w]).split()

	for w in to_write:
		print(len(w), w)
	# sort the strings in the descinding order by the frequency
	to_write = sorted(to_write, key=lambda  w: int(w[-1]), reverse=True)
	# header string
	string = 'MWE, pattern, sentiment,resource, frequency'
	# split the header string by the words
	string = re.sub("[^\w]", " ", string).split()
	# insert the header string to the beginning of the list that will be written to csv file
	to_write.insert(0, string)

	# split mwe to two words
	for w in range(len(to_write)):
		to_write[w][0] = to_write[w][0] + ' ' + to_write[w][1]

	# move pattern, tonality, dict and frequency on the one cell to the left
	for i in range(len(to_write)):
		for j in range(1, len(to_write[i]) - 1):
			to_write[i][j] = to_write[i][j + 1]
		# delete the last, now empty, column
		del to_write[i][-1]

	# write to csv
	with open(path, "w", newline="") as f:
		cw = csv.writer(f)
		cw.writerows(r for r in to_write)


if __name__ == "__main__":
	# reading the paths from the terminal

	rp = '/home/anna/Desktop/rusentilex_pos.txt'
	lp = '/home/anna/Desktop/linis_pos.txt'
	rev_p = '/home/anna/Desktop/otzovik_medicine.json'
	csv_p = '/home/anna/Desktop/adj_noun.csv'

	parser = argparse.ArgumentParser()
	parser.add_argument('rusentilex', type=str, help='path to rusentilex file', default= rp)
	parser.add_argument('linis', type=str, help='path to linis file', default=lp)
	parser.add_argument('reviews', type=str, help='path to reviews file', default=rev_p)
	parser.add_argument('csv_path', type=str, help='path where to write csv file', default=csv_p)

	parser.add_argument('adj_noun_flag', type=bool,
	                    help='if you want to find adj_noun bigrams -> type True, else ->False', default=False)
	parser.add_argument('neg_verb_flag', type=bool,
	                    help='if you want to find neg_verb bigrams -> type True, else ->False', default=False)
	parser.add_argument('neg_noun_flag', type=bool,
	                    help='if you want to find neg_noun bigrams -> type True, else ->False', default=False)
	parser.add_argument('neg_adj_flag', type=bool,
	                    help='if you want to find neg_adj bigrams -> type True, else ->False', default=True)
	args = parser.parse_args()

	rusentilex_path = args.rusentilex
	linis_path = args.linis
	reviews_path = args.reviews
	path = args.csv_path

	adj_noun = args.adj_noun_flag
	neg_verb = args.neg_verb_flag
	neg_noun = args.neg_noun_flag
	neg_adj= args.neg_adj_flag

	# rusentilex_path = rp
	# linis_path = lp
	# reviews_path = rev_p
	# csv_path= csv_p

	# adj_noun = True
	# neg_verb = False
	# neg_noun = False
	# neg_adj = False

	rusentilex = read_rusentilex_pos(rusentilex_path)
	linis = read_linis_pos(linis_path)
	# reading the reviews
	ub= []
	c =  0

	with codecs.open(reviews_path, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				print("processing review #", c)
				review = []
				doc = json.loads(line)
				review.append(doc['reviewText'])
				review = split_by_words(review)
				# getting the bigrams
				bigrams_for_work = bigrams(review, adj_noun=adj_noun, neg_verb=neg_verb, neg_noun=neg_noun,
				                           neg_adj=neg_adj)[1]
				tones = find_in_dict(bigrams_for_work, rusentilex, linis)
				# finding in which bigrams are the found words
				unique_bigram = unique_bigrams(bigrams_for_work, tones)
				ub.append(unique_bigram)
				c += 1

			except:
				pass
	ub = sum(ub, [])
	print("ub =", ub)
	for b in range(len(ub)):
		ub[b] = ', '.join(ub[b])
	print(ub)
	# count the number of the unique bigrams (frequency)
	counter = Counter(ub)
	print(counter)
	print("h")
	create_file_and_write_to_csv(counter, csv_path)