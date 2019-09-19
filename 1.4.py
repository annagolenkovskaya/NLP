"""Подсчитать число отзывов для каждого уникального значения в cat3"""
import codecs, json
from collections import Counter


def unique_reviews(fname):
	categories = []
	with codecs.open(fname, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				doc = json.loads(line)
				categories.append(doc['cat3'])

				print(len(categories))
			except:
				pass

	numbers = Counter(categories)
	return numbers


path = '/home/anna/Desktop/all_reviews_texts_lemm.txt'

result = unique_reviews(path)
keys = list(result.keys())
for i in range(len(keys)):
	print('Количество отзывов для категории ', keys[i], result[keys[i]])