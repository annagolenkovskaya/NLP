"""
Из всех словосочетаний пункта 2 выбрать те, где:
первое слово - прилагательное, второе - существительное [Прил. + Сущ.]
первое слово - причастие, второе - существительное [Прич. + Сущ.]
первое слово - существительное, второе - сущ. в родительном падеже [Сущ. + Сущ., Род.п.]
первое слово - существительное, второе - сущ. в творительном падеже [Сущ. + Сущ., Твор.п.]
первое слово - отрицание, второе - глагол
Записать результаты п.2 в текстовый файл. Вывести цифры:
сколько всего извлеклось словосочетаний
сколько осталось словосочетаний после 2
сколько словосочетаний каждого типа 2а-2d
"""

import pymorphy2, re, argparse
from collections import Counter
from utils import read_reviews, read_linis, read_rusentilex, read_rusentilex_pos


def dict_pos(dict, maturity=False):
	parser = argparse.ArgumentParser()
	parser.add_argument('path_to', type=str, help='path where the file with parts of speech dictionaty will be kept')
	args = parser.parse_args()
	path_to = args.path_to
	# path_to = '/home/anna/Desktop/rusentilex_pos.txt'
	dict = read_rusentilex()
	# path_to = '/home/anna/Desktop/linis_pos.txt'
	# dict = read_linis()

	morph = pymorphy2.MorphAnalyzer()
	for line in range(len(dict)):
		tag = morph.tag(str(dict[line]))[0]

		if 'NOUN'in tag:
			dict[line] += '_NOUN'
			if maturity:
				dict[line] += '_{}'.format(tag.case)
		elif 'ADJF'in tag:
			dict[line] += '_ADJ'
		elif 'ADJS'in tag:
			dict[line] += '_ADJ'
		elif 'COMP'in tag:
			dict[line] += '_ADJ'
		elif 'VERB'in tag:
			dict[line] += '_VERB'
		elif 'INFN' in tag:
			dict[line] += '_VERB'
		elif 'PRTF' in tag:
			dict[line] += '_PART'
		elif 'PRTS' in tag:
			dict[line] += '_PART'
		elif 'GRND' in tag:
			dict[line] += '_PART'
		elif 'NUMR' in tag:
			dict[line] += '_NUM'
		elif 'ADVB' in tag:
			dict[line] += '_ADV'
		elif 'NPRO' in tag:
			dict[line] += '_PRON'
		elif 'PRED' in tag:
			dict[line] += '_ADV'
		elif 'PREP' in tag:
			dict[line] += '_ADV'
		elif 'CONJ' in tag:
			dict[line] += '_SCONJ'
		elif 'PRCL' in tag:
			dict[line] += '_INTJ'
		elif 'INTJ' in tag:
			dict[line] += '_INTJ'

	with open(path_to, "w") as f:
		for r in dict:
			f.write(str(r) + '\n')

	return dict


def bigrams(reviews, adj_noun=False, part_noun=False, neg_verb=False, noun_noun_gent=False,
            noun_noun_ablt=False):
	parser = argparse.ArgumentParser()
	parser.add_argument('path_to', type=str, help='path where to write the file with bigrams data')
	args = parser.parse_args()
	path_to = args.path_to

	# path_to = '/home/anna/Desktop/frequencies_adj_noun.txt'
	bigrams = []
	all_res = []
	number_of_all_bigrams = 0
	all_bigrams = 0
	all_adj_noun_bigrams = 0
	all_part_noun_bigrams = 0
	all_noun_noun_gent_bigrams = 0
	all_noun_noun_ablt_bigrams = 0

	for review in reviews:
		for word in range(1, len(review)):
			words = []
			words.append(review[word - 1])
			words.append(review[word])
			bigrams.append(words)

		res = []
		number_of_bigrams = 0

		if adj_noun:
			adj_noun_bigrams = []
			for bigram in bigrams:
				if 'ADJ' in bigram[0] and 'NOUN' in bigram[1]:
					adj_noun_bigrams.append(bigram)
			res = adj_noun_bigrams.copy()

		if part_noun:
			part_noun_bigrams = []
			for bigram in bigrams:
				if 'PART' in bigram[0] and 'NOUN' in bigram[1]:
					part_noun_bigrams.append(bigram)
			res += part_noun_bigrams.copy()

		if noun_noun_gent:
			noun_noun_gent_bigrams = []
			for bigram in bigrams:
				if 'NOUN' in bigram[0] and 'NOUN_gent' in bigram[1]:
					noun_noun_gent_bigrams.append(bigram)
			res += noun_noun_gent_bigrams.copy()

		if noun_noun_ablt:
			noun_noun_ablt_bigrams = []
			for bigram in bigrams:
				if 'NOUN' in bigram[0] and 'NOUN_ablt' in bigram[1]:
					noun_noun_ablt_bigrams.append(bigram)
			res += noun_noun_ablt_bigrams.copy()

		if neg_verb:
			neg_verb_bigrams = []
			for bigram in bigrams:
				if 'не_INTJ' in bigram[0] and 'VERB' in bigram[1]:
					neg_verb_bigrams.append(bigram)
			res += neg_verb_bigrams
			number_of_bigrams += len(res)

	all_res.append(res)
	number_of_all_bigrams += number_of_bigrams
	all_bigrams += len(bigrams)
	all_adj_noun_bigrams += len(adj_noun_bigrams)
	all_part_noun_bigrams += len(part_noun_bigrams)
	all_noun_noun_gent_bigrams += len(noun_noun_gent_bigrams)
	all_noun_noun_ablt_bigrams += len(noun_noun_ablt_bigrams)
	all_res.append('Всего извлеклось {} биграм'.format(number_of_all_bigrams))
	all_res.append('Осталось {} биграм'.format(all_bigrams - number_of_all_bigrams))
	all_res.append('Словосочетаний прилагательное + существительное = {}'.format(all_adj_noun_bigrams))
	all_res.append('Словосочетаний причастие + существительное = {}'.format(all_part_noun_bigrams))
	all_res.append('Словосочетаний существительное + существительное в родительном падеже = {}'.
	           format(all_noun_noun_gent_bigrams))
	all_res.append('Словосочетаний существительное + существительное в творительном падеже = {}'.
	           format(all_noun_noun_ablt_bigrams))

	with open(path_to, "w") as f:
		for r in all_res:
			f.write(str(r) + '\n')

	return bigrams, all_res


def rusentilex_tonality(file, bigrams, pos=False, neg=False):
	parser = argparse.ArgumentParser()
	parser.add_argument('path_to', type=str, help='path to file where to write the results')
	args = parser.parse_args()
	path_to = args.path_to
	# path_to = '/home/anna/Desktop/positives.txt'
	# path_to = '/home/anna/Desktop/negatives.txt'

	positives = []
	negatives = []

	for bigram in bigrams:
		for line in file:
			if bigram[1] == line[0] or bigram[0] == line[0]:
				if pos:
					if 'positive' in line:
						positives.append(bigram)
						break

				if neg:
					if 'negative' in line:
						negatives.append(bigram)
						break

	if pos:
		for bigram in range(len(positives)):
			positives[bigram] = positives[bigram][0] + ' ' + positives[bigram][1]
		counter = Counter(positives)
		counter_list = []
		keys = list(counter.keys())
		for i in range(len(keys)):
			counter_list.append({keys[i]: counter[keys[i]]})

		with open(path_to, "w") as f:
			for r in counter_list:
				f.write(str(r) + '\n')

	if neg:
		for bigram in range(len(negatives)):
			negatives[bigram] = negatives[bigram][0] + ' ' + negatives[bigram][1]
		counter = Counter(negatives)
		counter_list = []
		keys = list(counter.keys())
		for i in range(len(keys)):
			counter_list.append({keys[i]: counter[keys[i]]})
		with open(path_to, "w") as f:
			for r in counter_list:
				f.write(str(r) + '\n')


if __name__ == "__main__":
	# dict_pos()

	reviews = read_reviews()
	reviews = reviews[:100]
	reviews_to_process = []
	for review in range(len(reviews)):
		reviews[review] = [reviews[review]['description'], reviews[review]['lemm_text']]

		try:
			reviews[review][0] = re.sub("[^\w]", " ", reviews[review][0]).split()
			reviews[review][1] = re.sub("[^\w]", " ", reviews[review][1]).split()
		except:
			pass

		reviews[review] = dict_pos(reviews[review][1], maturity=False)

	bigrams = bigrams(reviews, adj_noun=False, part_noun=False, noun_noun_gent=False, noun_noun_ablt=False,
	                  neg_verb=False)

	file = read_rusentilex_pos()

	rusentilex_tonality(file, bigrams[0], pos=False, neg=True)