from flair.data import Dictionary
from flair.models import LanguageModel
from flair.trainers.language_model_trainer import LanguageModelTrainer, TextCorpus
import pickle

# are you train a forward or backward LM?
is_forward_lm = True

dictionaty = Dictionary.load_from_file('/home/anna/Desktop/markup/learning/dictionary/dict')

# get your corpus, process forward and at the character level
corpus = TextCorpus('/home/anna/Desktop/markup/learning', dictionaty, is_forward_lm, character_level=True)

# instantiate your language model, set hidden size and number of layers
language_model = LanguageModel(dictionaty, is_forward_lm, hidden_size=128, nlayers=1)

# train your language model
trainer = LanguageModelTrainer(language_model, corpus)

trainer.train('resources/taggers/language_model', sequence_length=10, mini_batch_size=10, max_epochs=10)