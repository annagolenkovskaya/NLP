# -*- coding: utf-8 -*-
"""a. Для слов с положительной и негативной окраской из каждого словаря посчитать:
частоту слов в отзывах разных рейтингов (всего 5 рейтингов = 5 разных таблиц).
Результаты записать в csv файлы (аргумент скрипта), формат: слово, тональность, источник (linis or rusentilex), частота
b. То же самое, но теперь просуммировать частоты слов с одной окраской в отзывах каждого рейтинга. Записать результаты.
"""

import codecs, json, pandas as pd, csv, re, argparse
from collections import Counter
from utils import read_reviews, read_rusentilex, read_linis


def tonality(rating, write_all_words=False, sum_pos_neg=False):
	reviews= read_reviews()

	# csv_path = '/home/anna/Desktop/tonalities_rating_one.csv'
	rating_two_path = '/home/anna/Desktop/tonalities_rating_two.csv'
	rating_three_path = '/home/anna/Desktop/tonalities_rating_three.csv'
	rating_four_path = '/home/anna/Desktop/tonalities_rating_four.csv'
	rating_five_path = '/home/anna/Desktop/tonalities_rating_five.csv'

	ratings_sum_one_path = '/home/anna/Desktop/tonalities_ratings_sum_one.csv'
	ratings_sum_two_path = '/home/anna/Desktop/tonalities_ratings_sum_two.csv'
	ratings_sum_three_path = '/home/anna/Desktop/tonalities_ratings_sum_three.csv'
	ratings_sum_four_path = '/home/anna/Desktop/tonalities_ratings_sum_four.csv'
	ratings_sum_five_path = '/home/anna/Desktop/tonalities_ratings_sum_five.csv'
	parser = argparse.ArgumentParser()
	parser.add_argument('csv_path', type=str, help='path to csv file')
	args = parser.parse_args()
	csv_path = args.csv_path

	data_by_rating = []
	for review in reviews:
		if re.search('Общий рейтинг.*?(\d)', str(review['product-rating'])).group(1) == rating:
			data_by_rating.append(review['lemm_text'])

	print("here")
	words_by_rating = []
	for text in data_by_rating:
		words_by_rating.append(text.split(' '))
	print("here")
	print(words_by_rating)
	# for text in range(len(words_by_rating)):
	# 	for word in range(len(words_by_rating[text])):
	# 		words_by_rating[text][word] = words_by_rating[text][word][:words_by_rating[text][word].find("_")]
	print(words_by_rating)
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
	linis_tonalities = read_linis()
	rusentilex = read_rusentilex()

	for word in words_by_rating:
		print("word =", len(word), word)
		for line in linis_tonalities:
			if word == line[0]:
				print("linis line =", len(line), line)
				if line[1] == 'negative':
					tone = [word, 'neg', 'linis', counter[word]]
					tones.append(tone)
					found.append(word)

				elif line[1] == 'positive':
					tone = [word, 'pos', 'linis', counter[word]]
					tones.append(tone)
					found.append(word)

				print("tones =", tones)

		if word not in found:
			for line in rusentilex:
				if word == line[0]:
					print("rusenti line =", len(line), line)

					if line[1] == 'positive':
						tone = [word, 'pos', 'rusentilex', counter[word]]
						tones.append(tone)

					elif line[1] == 'negative':
						tone = [word, 'neg', 'rusentilex', counter[word]]
						tones.append(tone)
						print("tones =", tones)

	for l in range(len(tones) - 1, 0, -1):
		if tones[l] == tones[l - 1]:
			tones.remove(tones[l])

	if sum_pos_neg:
		positives = 0
		negatives = 0

		for line in tones:
			print(len(line), line)
			if 'pos' in line:
				positives += line[3]
				print("positives =", positives)
			elif 'neg'in line:
				negatives += line[3]
				print("negatives =", negatives)

		sum_pos_neg = [['positives = {}'.format(positives)], ['negatives = {}'.format(negatives)]]
		print("sum_pos_neg = ", sum_pos_neg)

		with open(csv_path, "w", newline="") as f:
			cw = csv.writer(f)
			cw.writerows(s for s in sum_pos_neg)

	if write_all_words:
		with open(csv_path, "w", newline="") as f:
			cw = csv.writer(f)
			cw.writerows(r for r in tones)


if __name__ == "__main__":
	tonality(rating='1', write_all_words=True, sum_pos_neg=False)