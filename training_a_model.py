from flair.data import Corpus, Sentence
from flair.datasets import WIKINER_RUSSIAN
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, FlairEmbeddings
from typing import List

# 1. get the corpus
corpus: Corpus = WIKINER_RUSSIAN().downsample(0.05)
print(corpus)

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
embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256, embeddings=embeddings, tag_dictionary=tag_dictionary,
                                        tag_type=tag_type, use_crf=True)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
trainer.train('/home/anna/Desktop/markup/collection5_learning/model', learning_rate=0.1, mini_batch_size=32,
              max_epochs=150)

# 8. plot weight traces (optional)
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_weights('/home/anna/Desktop/markup/collection5_learning/model/weights.txt')
