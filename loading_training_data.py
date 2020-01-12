import flair.datasets
corpus = flair.datasets.IMDB()
print(corpus)
# english_corpus = flair.datasets.UD_ENGLISH()
# german_corpus = flair.datasets.UD_GERMAN()
# russian_corpus = flair.datasets.UD_RUSSIAN()

# make a multi corpus consisting of three UDs
# from flair.data import MultiCorpus
# multi_corpus = MultiCorpus([english_corpus, german_corpus, russian_corpus])
# downsampled_corpus = flair.datasets.UD_ENGLISH().downsample(0.1)

# create tag dictionary for a PoS task
# print(corpus.make_tag_dictionary('upos'))

# create tag dictionary for an NER task
# corpus = flair.datasets.WIKINER_RUSSIAN()
# print(corpus)
# print(corpus.make_tag_dictionary('ner'))

# create label dictionary for a text classification task
# corpus = flair.datasets.TREC_6()
# print(corpus.make_label_dictionary())

# corpus = flair.datasets.TREC_6()
# stats = corpus.obtain_statistics()
# print(stats)

# print("--- 1 Original ---")
# print(corpus)

# print("---2 Downsampled ---")
# print(downsampled_corpus)
# print the number of Sentences in the train split
# print(len(corpus.train))

# print the number of Sentences in the test split
# print(len(corpus.test))

# print the number of Sentences in the dev split
# print(len(corpus.dev))

# print the first Sentence in the training split
# print(corpus.test[0])

# print the first sentence in the training split
# print(corpus.test[0].to_tagged_string('pos'))

# corpus = flair.datasets.UD_RUSSIAN()

# print the number of Sentences in the train split
# print(len(corpus.train))

# print the number of Sentences in the test split
# print(len(corpus.test))

# print the number of Sentences in the dev split
# print(len(corpus.dev))

# print the first Sentence in the training split
# print(corpus.test[0])

# print the first sentence in the training split
# print(corpus.test[0].to_tagged_string('pos'))
