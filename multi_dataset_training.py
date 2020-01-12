#  not multi already

from typing import List
from flair.data import Corpus
from flair.datasets import UD_ENGLISH, UD_RUSSIAN
from flair.embeddings import FlairEmbeddings, TokenEmbeddings, StackedEmbeddings
from flair.training_utils import EvaluationMetric

# 1. get the corpora - English and Russian UD
corpus: Corpus = UD_RUSSIAN().downsample(0.00625)

# 2. what tag do we want to predict?
tag_type = 'upos'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dictionary.idx2item)

# 4. initialize embeddings
embedding_types: List[TokenEmbeddings] = [# we use multilingual Flair embeddings in the task
FlairEmbeddings('multi-forward'), FlairEmbeddings('multi-backward'), ]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=256, embeddings=embeddings, tag_dictionary=tag_dictionary,
                                        tag_type=tag_type, use_crf=True)

# 8. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus)

# 7. start training
trainer.train( '/home/anna/Desktop/markup/multi', learning_rate=0.1, mini_batch_size=32, max_epochs=150,)
