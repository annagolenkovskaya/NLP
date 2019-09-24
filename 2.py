"""Для слов с положительной и негативной окраской из каждого словаря посчитать:
частоту слов в отзывах разных рейтингов (всего 5 рейтингов = 5 разных таблиц).
Результаты записать в csv файлы (аргумент скрипта), формат: слово, тональность, источник (linis or rusentilex), частота
"""

import codecs, json, pandas as pd, csv
from collections import Counter

path = '/home/anna/Desktop/otzovik_medicine.json'
linis = '/home/anna/Desktop/collection (docs&words)_2016_all_labels/full word_rating_after_coding.xlsx'
rusentilex_path = '/home/anna/Desktop/rusentilex.txt'

data = pd.ExcelFile(linis)
dfs = {sheet_name: data.parse(sheet_name)
       for sheet_name in data.sheet_names}
linis_tonalities = dfs['Лист1']
linis_tonalities = linis_tonalities.values.tolist()
print("linis_tonalities =", type(linis_tonalities))

rusentilex = []
with open(rusentilex_path) as text:
	for line in text:
		rusentilex.append(line)
rusentilex = rusentilex[18:]


def tonality(csv_path):
	reviews = []
	with codecs.open(path, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				doc = json.loads(line)
				reviews.append({doc['overall']: doc['reviewText']})

			except:
				pass

		one = []
		two = []
		three = []
		four = []
		five = []

		for review in reviews:
		# 	try:
		# 		one.append(review['1'])
		# 	except:
		# 		pass
			# try:
			# 	two.append(review['2'])
			# except:
			# 	pass
			# try:
			# 	three.append(review['3'])
			# except:
			# 	pass
			# try:
			# 	four.append(review['4'])
			# except:
			# 	pass
			try:
				five.append(review['5'])
			except:
				pass

	print("here")

	words_by_rating = []
	for text in five:  # this part changes for every rating value
		words_by_rating.append(text.split(' '))
	print("here")

	for text in range(len(words_by_rating)):
		for word in range(len(words_by_rating[text])):
			words_by_rating[text][word] = words_by_rating[text][word][:words_by_rating[text][word].find("_")]
	print("here")

	for text in range(len(words_by_rating)):
		for word in range(len(words_by_rating[text]) - 1, -1, -1):
			if not words_by_rating[text][word].isalnum():
				del words_by_rating[text][word]
	print("here")

	words_by_rating = sum(words_by_rating, [])

	counter = Counter(words_by_rating)
	print(counter, len(counter))

	words_by_rating = set(words_by_rating)
	tones = []
	found = []

	print("here")
	for word in words_by_rating:
		print("word =", len(word), word)
		for line in linis_tonalities:
			if word in line:
				print("linis line =", len(line), line)
				if line[1] < 0:
					tone = [word, 'neg', 'linis', counter[word]]
					tones.append(tone)
					found.append(word)

				elif line[1] > 0:
					tone = [word, 'pos', 'linis', counter[word]]
					tones.append(tone)
					found.append(word)

				print("tones =", tones)

		if word not in found:
			for line in rusentilex:
				if line[:len(word)] == word and line[len(word):len(word) + 1] == ',':
					print(line[:len(word)], line[len(word):len(word) + 1])
					print("rusenti line =", len(line), line)

					if 'positive' in line:
						tone = [word, 'pos', 'rusentilex', counter[word]]
						tones.append(tone)

					elif 'negative' in line:
						tone = [word, 'neg', 'rusentilex', counter[word]]
						tones.append(tone)
						print("tones =", tones)

	for l in range(len(tones) - 1, 0, -1):
		if tones[l] == tones[l - 1]:
			tones.remove(tones[l])

	with open(csv_path, "w", newline="") as f:
		cw = csv.writer(f)
		cw.writerows(r for r in tones)


rating_one_path = '/home/anna/Desktop/tonalities_rating_one.csv'
rating_two_path = '/home/anna/Desktop/tonalities_rating_two.csv'
rating_three_path = '/home/anna/Desktop/tonalities_rating_three.csv'
rating_four_path = '/home/anna/Desktop/tonalities_rating_four.csv'
rating_five_path = '/home/anna/Desktop/tonalities_rating_five.csv'
tonality(csv_path=rating_five_path)