
from flair.models import SequenceTagger
from flair.data import Sentence

# load the model you trained
model = SequenceTagger.load('/home/anna/Desktop/markup/multi/final-model.pt')

# create example sentence
sentence = Sentence('Я хочу спать')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())