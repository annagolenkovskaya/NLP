from flair.data import Corpus, Sentence
from flair.datasets import WIKINER_RUSSIAN, ColumnCorpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, FlairEmbeddings
from typing import List

# 1. get the corpus
# corpus: Corpus = WIKINER_RUSSIAN().downsample(0.05)
# print(corpus)

# define columns
columns = {4: 'text', 1: 'ner'}

# this is the folder in which train, test and dev files reside
data_folder = '/home/anna/Desktop/markup/brat_data'

# init a corpus using column format, data folder and the names of the train, dev and test files
corpus: Corpus = ColumnCorpus(data_folder, columns, train_file='train.txt', test_file='test.txt', dev_file='dev.txt')
print(corpus)
print(len(corpus.train[0]))
print(corpus.train[0].to_tagged_string('ner'))
print(corpus.train[0].to_tagged_string('text'))

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)

# 4. initialize embeddings
embedding_types = WordEmbeddings('ru-wiki')
# embedding_types: List[TokenEmbeddings] = [WordEmbeddings('ru-wiki'),
                                          # comment in this line to use character embeddings
                                          # CharacterEmbeddings(), # comment in these lines to use flair embeddings
                                          # FlairEmbeddings('news-forward'), # FlairEmbeddings('news-backward'),
 # ]
# embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256, embeddings=embedding_types, tag_dictionary=tag_dictionary,
                                        tag_type=tag_type, use_crf=True)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
trainer.train('/home/anna/Desktop/markup/brat_data/model', learning_rate=0.1, mini_batch_size=32,
              max_epochs=150)

# 8. plot weight traces (optional)
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_weights('/home/anna/Desktop/markup/brat_data/model/weights.txt')
