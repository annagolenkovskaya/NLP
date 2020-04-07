import pandas, operator, pymorphy2
from flair.embeddings import WordEmbeddings
import numpy as np


def build_vocab(X):
	tweets = X.apply(lambda s: s.split()).values
	vocab = {}

	for tweet in tweets:
		for word in tweet:
			try:
				vocab[word] += 1
			except KeyError:
				vocab[word] = 1
	return vocab


test = '/home/anna/Desktop/markup/brat_data/marked/train/test.txt'
test_df = pandas.read_csv(test, sep='\t', header=None)
morph = pymorphy2.MorphAnalyzer()
# print(pandas.read_csv('/home/anna/.flair/embeddings/ru-wiki-fasttext-300d-1M').head())
test_df[0] = test_df[0].apply(lambda x: morph.parse(x.lower())[0].normal_form)

vocab = build_vocab(test_df[0])
print(len(vocab))
# word_is_covered = {vocab.keys():[0]*len(vocab)}
word_is_covered = {el:0 for el in vocab.keys()}
print(word_is_covered)

with open('/home/anna/Downloads/wiki.ru.vec') as f:
	for x in f:
		word = morph.parse(x.split()[0])[0].normal_form
		if word in word_is_covered.keys():
			print(word)
			word_is_covered[word] =1


vocab_covered = sum(word_is_covered.values())/len(word_is_covered)
print(str(round(vocab_covered*100,2))+"% of words in vocabulary is covered")
words_covered = 0
text_length = 0
for word in vocab.keys():
	words_covered += vocab[word]*word_is_covered[word]
	text_length += vocab[word]

text_covered = words_covered/ text_length
print(str(round(text_covered*100,2))+"% of text is covered")

# def check_embeddings_coverage(X, embeddings):
# 	vocab = build_vocab(X)

	# covered = {}
	# oov = {}
	# n_covered = 0
	# n_oov = 0

	# for word in vocab:
		# print(embeddings[word])
		# try:
		# 	covered[word] = embeddings[word]
		# 	n_covered += vocab[word]
		# except:
		# 	oov[word] = vocab[word]
		# 	n_oov += vocab[word]

	# vocab_coverage = len(covered) / len(vocab)
	# text_coverage = (n_covered / (n_covered + n_oov))

	# sorted_oov = sorted(oov.items(), key=operator.itemgetter(1))[::-1]  # непокрытые слова
	# return sorted_oov, vocab_coverage, text_coverage

# test_data = []
# with open(test, 'r') as f:
# 	test_data = f.readlines()
# print(len(test_data), test_data)
#
# for t in range(len(test_data)):
# 	test_data[t] = test_data[t].replace(' ', '\t')
# print(len(test_data), test_data)
# with open(test, 'w') as f:
# 	f.writelines(test_data)

# print(test_df[0])
# embedding_types = WordEmbeddings('ru-wiki')
# fasttext_embeddings = np.load('/home/anna/.flair/embeddings/ru-wiki-fasttext-300d-1M', allow_pickle=True)
# print(fasttext_embeddings['город'])
# print(check_embeddings_coverage(test_df[0], fasttext_embeddings)[1])
# print(check_embeddings_coverage(test_df[0], fasttext_embeddings)[2])

