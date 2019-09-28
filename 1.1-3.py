# -*- coding: utf-8 -*-
"""Открыть файл reviews_texts.txt (аргумент скрипта). Каждая строка файла представляет собой json объект (отзыв).
Выбрать все отзывы, где  "cat2": "Лекарственные средства" (аргумент скрипта).
Из поля product-rating извлечь рейтинг (написать регулярное выражение для извлечения числа)
Подсчитать число отзывов для каждого уникального значения рейтинга
"""
import re, argparse
from collections import Counter
from utils import read_reviews

# path = '/home/anna/Desktop/all_reviews_texts_lemm.txt'
# cat_value = 'Лекарственные средства'
parser = argparse.ArgumentParser()
parser.add_argument('cat', type=str, help='category name')
args = parser.parse_args()
cat_value = args.cat


def rating(cat_value, by_cat=False, ratings=False, number_of_units=False):
	product_ratings =[]
	units = 0
	reviews = read_reviews()
	found = []
	for review in reviews:
		if by_cat:
			if review['cat2'] == cat_value:
				found.append(review)

		if ratings or number_of_units:
			try:
				product_ratings.append(re.search('Общий рейтинг.*?(\d)', str(review['product-rating'])).group(1))
			except:
				continue

		if number_of_units:
			units = Counter(product_ratings)

	return found, product_ratings, units


rate = rating(cat_value, by_cat=True, ratings=False, number_of_units=False)
print('Количество отзывов, где cat2: Лекарственные средства =', len(rate[0]))
print('Рейтинги =', rate[1], len(rate[1]))
print("Количество отзывов по рейтингам: '5':", rate[2]['5'],
      ", '4':", rate[2]['4'], ", '3':",rate[2]['3'], ", '2':", rate[2]['2'], ", '1':",rate[2]['1'])