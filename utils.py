import codecs, json, argparse, sys


def read_rusentilex(file):

	pass


def read_linis(file):
	pass


def read_reviews():
	parser = argparse.ArgumentParser()
	parser.add_argument('indir', type=str)
	args = parser.parse_args()
	path = args.indir
	reviews = []
	with codecs.open(path, "r", encoding='utf-8') as fin:
		for line in fin:
			try:
				doc = json.loads(line)
				reviews.append([doc['description'], doc['lemm_text']])

			except:
				pass

	return reviews


read_reviews()