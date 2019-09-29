import codecs, json, argparse, re, pandas as pd


def read_rusentilex():
	# path = '/home/anna/Desktop/rusentilex.txt'
	parser = argparse.ArgumentParser()
	parser.add_argument('rusentilex', type=str, help='path to rusentilex file')
	args = parser.parse_args()
	path = args.rusentilex

	rusentilex = []
	with open(path) as text:
		for line in text:
			rusentilex.append(line)
	rusentilex = rusentilex[18:]

	for line in range(len(rusentilex)):
		rusentilex[line] = re.sub("[^\w]", " ", rusentilex[line]).split()
		rusentilex[line] = rusentilex[line][0] + ', ' + rusentilex[line][3]
		rusentilex[line] = re.sub("[^\w]", " ", rusentilex[line]).split()
	return rusentilex


def read_rusentilex_pos():
	parser = argparse.ArgumentParser()
	parser.add_argument('rusentilex', type=str, help='path to rusentilex file')
	args = parser.parse_args()
	path = args.rusentilex
	# path = '/home/anna/Desktop/rusentilex_pos.txt'
	rusentilex = []

	with open(path) as text:
		for line in text:
			rusentilex.append(line)

	for line in range(len(rusentilex)):
		rusentilex[line] = re.sub("[^\w]", " ", rusentilex[line]).split()

	return rusentilex


def read_linis():
	parser = argparse.ArgumentParser()
	parser.add_argument('linis', type=str, help='path to rusentilex file')
	args = parser.parse_args()
	path = args.linis
	# path = '/home/anna/Desktop/collection (docs&words)_2016_all_labels/full word_rating_after_coding.xlsx'

	data = pd.ExcelFile(path)
	dfs = {sheet_name: data.parse(sheet_name)
	       for sheet_name in data.sheet_names}

	linis_tonalities = dfs['Лист1']
	linis_tonalities = linis_tonalities.values.tolist()
	linis = []

	for l in range(len(linis_tonalities)):
		if linis_tonalities[l][1] > 0:
			linis_tonalities[l][1] = 'positive'
		elif linis_tonalities[l][1] < 0:
			linis_tonalities[l][1] = 'negative'
	for l in linis_tonalities:
		if l[1] == 'positive' or l[1] == 'negative':
			linis.append(l)
	return linis


def read_reviews():
	parser = argparse.ArgumentParser()
	parser.add_argument('indir', type=str, help='path to reviews file')
	args = parser.parse_args()
	path = args.indir
	# path = '/home/anna/Desktop/cutted_reviews/all_reviews_texts_lemm_50000.txt'

	reviews = []
	with codecs.open(path, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				doc = json.loads(line)
				reviews.append(doc)

			except:
				pass

	return reviews