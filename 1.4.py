# -*- coding: utf-8 -*-
"""Подсчитать число отзывов для каждого уникального значения в cat3"""
import codecs, json
from collections import Counter
from utils import read_reviews


def unique_reviews(fname):
	categories = []
	reviews = read_reviews()
	for review in reviews:
		categories.append(review['cat3'])

	numbers = Counter(categories)
	return numbers


path = '/home/anna/Desktop/all_reviews_texts_lemm.txt'

result = unique_reviews(path)
keys = list(result.keys())
for i in range(len(keys)):
	print('Количество отзывов для категории ', keys[i], result[keys[i]])