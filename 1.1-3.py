"""Открыть файл reviews_texts.txt (аргумент скрипта). Каждая строка файла представляет собой json объект (отзыв).
Выбрать все отзывы, где  "cat2": "Лекарственные средства" (аргумент скрипта).
Из поля product-rating извлечь рейтинг (написать регулярное выражение для извлечения числа)
Подсчитать число отзывов для каждого уникального значения рейтинга
"""
import re
from collections import Counter

path = '/home/anna/Desktop/all_reviews_texts_lemm.txt'
cat_value = 'Лекарственные средства'


def rating(path, cat_value, by_cat=False, ratings=False, number_of_units=False):
	reviews = []
	product_ratings =[]

	with open(path) as text:
		for line in text:
			if by_cat:
				if cat_value in line:
					reviews.append(line)
			if ratings or number_of_units:
				try:
					product_ratings.append(re.search('Общий рейтинг.*?(\d)', line).group(1))
				except:
					continue

		if number_of_units:
			units = Counter(product_ratings)

	return reviews, product_ratings, units


rate = rating(path, cat_value, by_cat=False, ratings=False, number_of_units=True)
print('Количество отзывов, где cat2: Лекарственные средства =', len(rate[0]))
print('Рейтинги =', rate[1], len(rate[1]))
print("Количество отзывов по рейтингам: '5':", rate[2]['5'],
      ", '4':", rate[2]['4'], ", '3':",rate[2]['3'], ", '2':", rate[2]['2'], ", '1':",rate[2]['1'])