from flair.embeddings import FlairEmbeddings, BertEmbeddings,StackedEmbeddings
from flair.data import Sentence

# init Flair embeddings
flair_forward_embedding = FlairEmbeddings('multi-forward')
flair_backward_embedding = FlairEmbeddings('multi-backward')

# init multilingual BERT
bert_embedding = BertEmbeddings('bert-base-multilingual-cased')

# now create the StackedEmbedding object that combines all embeddings
stacked_embeddings = StackedEmbeddings(embeddings=[flair_forward_embedding, flair_backward_embedding, bert_embedding])

sentence = Sentence('The grass is green .')

# Just embed a sentence using the StackedEmbedding as you would with any single embedding.
stacked_embeddings.embed(sentence)

# now check out the embedded tokens.
for token in sentence:
	print(token)
	print(token.embedding)