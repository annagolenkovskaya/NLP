from flair.embeddings import WordEmbeddings
from flair.data import Sentence

# init embedding
glove_embedding = WordEmbeddings('ru-crawl')

# create sentence.
sentence = Sentence('Я хочу каникулы .')

# embed a sentence using glove.
glove_embedding.embed(sentence)

# now check out the embed tokens.
# for token in sentence:
# 	print(token)
# 	print(token.embedding)

from flair.embeddings import FlairEmbeddings

# init embedding
flair_embedding_forward = FlairEmbeddings('news-forward')

# create a sentence
sentence = Sentence('The grass is green .')

# embed words in sentence
# print(flair_embedding_forward.embed(sentence))

from flair.embeddings import WordEmbeddings, CharacterEmbeddings, FlairEmbeddings, StackedEmbeddings

# init standard GloVe embedding
glove_embedding = WordEmbeddings('glove')

# init Flair forward and backwards embeddings
flair_embedding_forward = FlairEmbeddings('news-forward')
flair_embedding_backward = FlairEmbeddings('news-backward')

# create a StackedEmbedding object that combines glove and forward/backward flair embeddings
stacked_embeddings = StackedEmbeddings([glove_embedding, flair_embedding_forward, flair_embedding_backward])

# just embed a sentence using the StackedEmbedding as you with any single embedding.
stacked_embeddings.embed(sentence)

# now check out the embedded tokens.
for token in sentence:
	print(token)
	print(token.embedding)