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

import codecs, json, pymorphy2, pandas as pd, re

path = '/home/anna/Desktop/otzovik_medicine.json'
path_cosmetics = '/home/anna/Desktop/cutted_reviews/all_reviews_texts_lemm_100000.txt'

linis = '/home/anna/Desktop/collection (docs&words)_2016_all_labels/full word_rating_after_coding.xlsx'
rusentilex_path = '/home/anna/Desktop/rusentilex.txt'

data = pd.ExcelFile(linis)
dfs = {sheet_name: data.parse(sheet_name)
       for sheet_name in data.sheet_names}
linis_tonalities = dfs['Лист1']
linis_tonalities = linis_tonalities.values.tolist()
for line in range(len(linis_tonalities)):
	linis_tonalities[line] = linis_tonalities[line][0]

rusentilex = []
with open(rusentilex_path) as text:
	for line in text:
		rusentilex.append(line)
rusentilex = rusentilex[18:]
for line in range(len(rusentilex)):
	rusentilex[line] = rusentilex[line][:rusentilex[line].find(",")]


def read_reviews(path):
	reviews = []
	with codecs.open(path, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				doc = json.loads(line)
				reviews.append([doc['description'], doc['lemm_text']])

			except:
				pass

	return reviews


def dict_pos(dict, path_to, maturity=False):
	morph = pymorphy2.MorphAnalyzer()
	for line in range(len(dict)):
		tag = morph.tag(dict[line])[0]

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

	# with open(path_to, "w") as f:
	# 	for r in dict:
	# 		f.write(r + '\n')

	return dict


def bigrams(review, path_to, adj_noun=False, part_noun=False, neg_verb=False, noun_noun_gent=False,
            noun_noun_ablt=False):
	bigrams = []
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

	res.append('Всего извлеклось {} биграм'.format(number_of_bigrams))
	res.append('Осталось {} биграм'.format(len(bigrams) - number_of_bigrams))
	res.append('Словосочетаний прилагательное + существительное = {}'.format(len(adj_noun_bigrams)))
	res.append('Словосочетаний причастие + существительное = {}'.format(len(part_noun_bigrams)))
	res.append('Словосочетаний существительное + существительное в родительном падеже = {}'.
	           format(len(noun_noun_gent_bigrams)))
	res.append('Словосочетаний существительное + существительное в творительном падеже = {}'.
	           format(len(noun_noun_ablt_bigrams)))

	with open(path_to, "w") as f:
		for r in res:
			f.write(str(r) + '\n')

	return res

linis_path_to = '/home/anna/Desktop/linis_pos.txt'
rusentilex_path_to = '/home/anna/Desktop/rusentilex_pos.txt'

path_to = '/home/anna/Desktop/bigrams.txt'
reviews = read_reviews(path_cosmetics)
review = reviews[1]
review[0] = re.sub("[^\w]", " ", review[0]).split()
review = dict_pos(review[0], linis_path_to, maturity=True)
bigrams = bigrams(review, path_to, adj_noun=True, part_noun=True, noun_noun_gent=True, noun_noun_ablt=True,
                  neg_verb=True)
for b in bigrams:
	print("bigram =", b)
