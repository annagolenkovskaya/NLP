from flair.datasets import UD_RUSSIAN
from flair.embeddings import WordEmbeddings, FlairEmbeddings, TokenEmbeddings
from flair.trainers import ModelTrainer
from typing import List

# load your corpus
corpus = UD_RUSSIAN().downsample(0.00625)
print(corpus)

from hyperopt import hp
from flair.hyperparameter.param_selection import SearchSpace, Parameter

# define your search space
search_space = SearchSpace()
search_space.add(Parameter.EMBEDDINGS, hp.choice, options=[
	[WordEmbeddings('ru')], [FlairEmbeddings('news-forward'), FlairEmbeddings('news-backward')]])
search_space.add(Parameter.HIDDEN_SIZE, hp.choice, options=[32, 64, 128])
search_space.add(Parameter.RNN_LAYERS, hp.choice, options=[1, 2])
search_space.add(Parameter.DROPOUT, hp.uniform, low=0.0, high=0.5)
search_space.add(Parameter.LEARNING_RATE, hp.choice, options=[0.05, 0.1, 0.15, 0.2])
search_space.add(Parameter.MINI_BATCH_SIZE, hp.choice, options=[8, 16, 32])

from flair.hyperparameter.param_selection import TextClassifierParamSelector, OptimizationValue

# create the parameter selector
param_selector = TextClassifierParamSelector(
	corpus,
	False,
	'/home/anna/Desktop/markup/model_tuning',
	'lstm', max_epochs=50, training_runs=3, optimization_value=OptimizationValue.DEV_SCORE)

# start the optimization
param_selector.optimize(search_space, max_evals=100)

