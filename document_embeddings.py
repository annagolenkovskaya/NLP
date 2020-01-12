from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentPoolEmbeddings, Sentence, OneHotEmbeddings, \
	DocumentRNNEmbeddings

# initialize the word embeddings
glove_embedding = WordEmbeddings('glove')
flair_embedding_forward = FlairEmbeddings('news-forward')
flair_embedding_backward = FlairEmbeddings('news-backward')
# embeddings = OneHotEmbeddings(corpus)

glove_embedding = WordEmbeddings('glove')


# initialize the document embeddings, mode = mean
document_embeddings = DocumentPoolEmbeddings([glove_embedding],
                                              # flair_embedding_backward, flair_embedding_forward],
                                             # pooling='min',
                                             fine_tune_mode='nonlinear')
document_embeddings = DocumentRNNEmbeddings([glove_embedding])

document_lstm_embeddings = DocumentRNNEmbeddings([glove_embedding], rnn_type='LSTM')

# create an example sentence
sentence = Sentence('The grass is green . And the sky is blue .')

# embed the sentence with our document embedding
document_embeddings.embed(sentence)

# now check out the embedded sentence.
print(sentence.get_embedding())