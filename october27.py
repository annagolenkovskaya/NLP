import pandas as pd, numpy as np,re, nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

psy_tar = '/home/anna/Downloads/Copy of PsyTAR_dataset.xlsx'
data = pd.ExcelFile(psy_tar)
dfs = {sheet_name: data.parse(sheet_name) for sheet_name in data.sheet_names}
review_id = list(dfs['Sample']['drug_id'])
sentence_labeling_id = list(dfs['Sentence_Labeling']['drug_id'])


def get_wordnet_pos(word):
	tag = nltk.pos_tag([word])[0][1][0].upper()
	tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}

	return tag_dict.get(tag, wordnet.NOUN)


def get_reviews():
	side_effect = dfs['Sample']['side-effect']
	for se in range(len(side_effect)):
		if type(side_effect[se]) == float:
			side_effect[se] = ''
		else:
			side_effect[se] = side_effect[se].lower()
	comment = dfs['Sample']['comment']
	for c in range(len(comment)):
		if type(comment[c]) == float:
			comment[c] = ''
		else:
			comment[c] = comment[c].lower()

	reviews = [x + ' ' + y for x, y in zip(side_effect, comment)]

	for r in range(len(reviews)):
		reviews[r] = re.sub("[^\w]", " ", reviews[r]).split()

	lemmatizer = WordNetLemmatizer()

	for r in range(len(reviews)):
		# print('reviews[{}] before ='.format(r), reviews[r])
		# print(reviews[r])
		for word in range(len(reviews[r])):
			# print('reviews[{}][{}] before ='.format(r, word),reviews[r][word])
			reviews[r][word] = lemmatizer.lemmatize(reviews[r][word], get_wordnet_pos(reviews[r][word]))
			# print('reviews[{}][{}] after ='.format(r, word),reviews[r][word])
	return reviews


def x_number(x):
	"""число сущностей типа X, X -- { ADR, WD, SSI, DI}
	оно же {X}_sent_number -- число предложений по каждому классу ADRs, WDs, SSIs, DIs, EF, and INF."""
	sentence_labeling_x = list(dfs['Sentence_Labeling'][x])
	x_dict = {}
	for i in range(len(sentence_labeling_id)):
		if sentence_labeling_id[i] not in x_dict.keys():
			x_dict[sentence_labeling_id[i]] = [sentence_labeling_x[i]]

		elif type(sentence_labeling_x[i]) == float and not np.isnan(sentence_labeling_x[i]) \
				and sentence_labeling_id[i] in x_dict.keys():
			x_dict[sentence_labeling_id[i]] += [sentence_labeling_x[i]]

	x_number = []
	for k, v in x_dict.items():
		is_nan = False
		for i in v:
			if type(i) == str or np.isnan(i):
				is_nan = True
		if not is_nan:
			x_number.append(len(v))
		else:
			x_number.append(len(v) - 1)
	return x_number[:-1]


def x_y_number(x, y):
	try:
		sheet_name = x + '_Mapped'
		drug_id = dfs[sheet_name]['drug_id']
	except KeyError:
		sheet_name = x + '-Mapped '
		drug_id = dfs[sheet_name]['drug_id']

	entity_type = dfs[sheet_name]['entity_type']

	entity_dict = {}
	for i in range(len(drug_id)):
		if type(drug_id[i]) == str and drug_id[i] not in entity_dict.keys():
			entity_dict[drug_id[i].lower()] = entity_type[i]
		else:
			if type(drug_id[i]) == str:
				entity_dict[drug_id[i].lower()] += ', ' + entity_type[i]
	part_num = []
	names = []
	for k, v in entity_dict.items():
		part_num.append(int(k[k.find(".") + 1:]))
		names.append(k[:k.find(".")])

	unique_names = []
	for n in range(1, len(part_num)):
		if part_num[n] < part_num[n -1]:
			unique_names.append(names[n - 1])
	unique_names.append(names[-1])

	num = []
	for i in review_id:
		num.append(int(i[i.find(".") + 1:]))
	ends = []

	for n in range(1, len(num)):
		if num[n] < num[n - 1]:
			ends.append(num[n - 1])

	ends.append(num[-1])
	names_by_count = []
	for e in range(len(ends)):
		for i in range(ends[e]):
			names_by_count.append(unique_names[e] + '.' + str(i + 1))
	entity_full_dict = {}

	for name in names_by_count:
		if name in entity_dict.keys():
			entity_full_dict[name] = re.sub("[^\w]", " ", entity_dict[name]).split()
		else:
			entity_full_dict[name] = ''

	necessary_entity_type = y.lower()

	count_list = []
	for v in entity_full_dict.values():
		count = 0
		for val in v:
			if val == necessary_entity_type:
				count += 1
		count_list.append(count)
	return count_list


def d_pos_neg_number(dict, pos=False, neg=False):
	"""{D}_{pos/neg}_number -- число положительных или негативных слов из словаря D"""
	bing_liu_neg_path = '/home/anna/Desktop/nlp resourses/dicts/liu_neg.txt'
	bing_liu_pos_path = '/home/anna/Desktop/nlp resourses/dicts/liu_pos.txt'
	mpqa_neg_path = '/home/anna/Desktop/nlp resourses/dicts/mpqa_neg.txt'
	mpqa_pos_path = '/home/anna/Desktop/nlp resourses/dicts/mpqa_pos.txt'

	if dict == 'bing_liu'and pos:
		dict_path = bing_liu_pos_path

	elif dict == 'bing_liu' and neg:
		dict_path = bing_liu_neg_path

	elif dict == 'mpqa' and pos:
		dict_path = mpqa_pos_path

	elif dict == 'mpqa' and neg:
		dict_path = mpqa_neg_path

	with open(dict_path, 'r') as f:
		dictionary = f.readlines()

	for d in range(len(dictionary)):
		dictionary[d] = dictionary[d].strip()

	reviews = get_reviews()
	coincidences = []
	for index, r in enumerate(reviews):
		print(index)
		count = 0
		for word in r:
			for w in dictionary:
				if w == word:
					count += 1

		coincidences.append(count)

	return coincidences


def words_number():
	reviews = get_reviews()
	word_number = []
	for r in reviews:
		word_number.append(len(r))

	return word_number


def sents_number():
	drug_id = dfs['Sentence_Labeling']['drug_id']
	sentence_index = dfs['Sentence_Labeling']['sentence_index']
	sent_dict= {}
	sent_number = []

	for i in range(len(drug_id)):
		sent_dict[drug_id[i]] = sentence_index[i]

	for v in sent_dict.values():
		sent_number.append(v)

	return sent_number[:-1]


rating = dfs['Sample']['rating']
xs= ['ADR', 'WD', 'SSI', 'DI']
x_numbers = []
for x in xs:
	x_numbers.append(x_number(x))

names = ['ADR_number', 'WD_number', 'SSI_number', 'DI_number']
ys = ['Physiological', 'Psychological', 'Cognitive', 'Functional']

x_y_numbers = []
for x in xs:
	for y in ys:
		x_y_numbers.append(x_y_number(x, y))

dicts = ['bing_liu', 'mpqa']
bing_liu_pos= d_pos_neg_number(dict=dicts[0], pos=True, neg=False)
bing_liu_neg = d_pos_neg_number(dict=dicts[0], pos=False, neg=True)
mpqa_pos = d_pos_neg_number(dict=dicts[1], pos=True, neg=False)
mpqa_neg = d_pos_neg_number(dict=dicts[1], pos=False, neg=True)

aditional_xs = ['EF', 'INF']

x_sent_numbers = []
for ax in aditional_xs:
	x_sent_numbers.append(x_number(ax))

word_number = words_number()

sent_number = sents_number()
res_df = pd.DataFrame({'ReviewID':review_id, 'Rating': rating, 'ADR_number': x_numbers[0], 'WD_number': x_numbers[1],
                       'SSI_number': x_numbers[2], 'DI_number': x_numbers[3],
                       'ADR_Physiological_number': x_y_numbers[0], 'ADR_Psychological_number': x_y_numbers[1],
                       'ADR_Cognitive_number': x_y_numbers[2], 'ADR_Functional_number': x_y_numbers[3],
                       'WD_Physiological_number': x_y_numbers[4], 'WD_Psychological_number': x_y_numbers[5],
                       'WD_Cognitive_number': x_y_numbers[6], 'WD_Functional_number': x_y_numbers[7],
                       'SSI_Physiological_number': x_y_numbers[8], 'SSI_Psychological_number': x_y_numbers[9],
                       'SSI_Cognitive_number': x_y_numbers[10], 'SSI_Functional_number': x_y_numbers[11],
                       'DI_Physiological_number': x_y_numbers[12], 'DI_Psychological_number': x_y_numbers[13],
                       'DI_Cognitive_number': x_y_numbers[14], 'DI_Functional_number': x_y_numbers[15],
                       'Bing_Liu_pos_number': bing_liu_pos, 'Bing_Liu_neg_number': bing_liu_neg,
                       'MPQA_pos_number': mpqa_pos, 'MPQA_neg_number': mpqa_neg, 'ADR_sent_number': x_numbers[0],
                       'WD_sent_number': x_numbers[1], 'SSI_sent_number': x_numbers[2],
                       'DI_sent_number': x_numbers[3], 'EF_sent_number': x_sent_numbers[0],
                       'INF_sent_number': x_sent_numbers[1], 'words_number': word_number, 'sents_number': sent_number
                       },
                      columns=['ReviewID', 'Rating',
                               'ADR_number', 'WD_number', 'SSI_number',
                               'DI_number', 'ADR_Physiological_number', 'ADR_Psychological_number',
                               'ADR_Cognitive_number', 'ADR_Functional_number','WD_Physiological_number',
                               'WD_Psychological_number', 'WD_Cognitive_number', 'WD_Functional_number',
                               'SSI_Physiological_number', 'SSI_Psychological_number', 'SSI_Cognitive_number',
                               'SSI_Functional_number', 'DI_Physiological_number', 'DI_Psychological_number',
                               'DI_Cognitive_number', 'DI_Functional_number', 'Bing_Liu_pos_number',
                               'Bing_Liu_neg_number', 'MPQA_pos_number', 'MPQA_neg_number', 'ADR_sent_number',
                               'WD_sent_number', 'SSI_sent_number', 'DI_sent_number', 'EF_sent_number',
                               'INF_sent_number', 'words_number', 'sents_number'])

# print(res_df)
# for d in res_df['Bing_Liu_pos_number']:
# 	print(d)
csv_path = '/home/anna/Desktop/df.csv'
res_df.to_csv(csv_path, sep=',', encoding='utf-8')