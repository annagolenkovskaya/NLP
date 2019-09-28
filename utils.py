import codecs, json, argparse, sys


def read_rusentilex(file):

	pass


def read_linis(file):
	pass


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


read_reviews()