from flair.data import Sentence
from flair.models import SequenceTagger

# load the model you trained
model = SequenceTagger.load('/home/anna/Desktop/markup/collection5_learning/model/final-model.pt')

# create example sentence
sentence = Sentence('Россия рассчитывает, что США воздействуют на Тбилиси в связи с обострением ситуации в зоне '
                    'грузино-осетинского конфликта')

# predict tags and print
model.predict(sentence)

print(sentence.to_tagged_string())