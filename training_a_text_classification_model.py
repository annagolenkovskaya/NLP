from flair.data import Corpus
from flair.datasets import TREC_6
from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentRNNEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer
from flair.data import Sentence

# 1. get the corpus
corpus: Corpus = TREC_6()

# 2. create the label dictionary
label_dict = corpus.make_label_dictionary()

# 3. make a list of word embeddings
word_embeddings = [WordEmbeddings('glove'), # comment in flair embrddings for state-of-the-art results
 # FlairEmbeddingd('news-forward'), # FlairEmbeddings('news-backward'),
]

# 4. initialize document embedding by passing list of word embeddings
# Can choose between many RNN types (GRU by default, to change use rnn_type parameter)
document_embeddings: DocumentRNNEmbeddings = DocumentRNNEmbeddings(word_embeddings, hidden_size=512,
                                                                   reproject_words=True, reproject_words_dimension=256,)

# 5. create the text classifier
classifier = TextClassifier(document_embeddings, label_dictionary=label_dict)

# 6. initialize the text classifier trainer
trainer = ModelTrainer(classifier, corpus)

# 7. start the training
trainer.train('/home/anna/Desktop/markup/8', learning_rate=0.1, mini_batch_size=32, anneal_factor=0.5, patience=5,
              max_epochs=150)

# 8. plot weight traces (optional)
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_weights('/home/anna/Desktop/markup/8/weights.txt')

classifier = TextClassifier.load('/home/anna/Desktop/markup/8/final-model.pt')

# create example sentences
sentence = Sentence('France is the current world cup winner.')

# predict class and print
classifier.predict(sentence)

print(sentence.labels)