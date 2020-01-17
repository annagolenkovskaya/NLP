from flair.data import Sentence
from flair.models import SequenceTagger

# load the model you trained
model = SequenceTagger.load('/home/anna/Desktop/markup/brat_data/model/best-model.pt')

# create example sentence
sentence = Sentence(u'Определяющим фактором повышения эффективности инновационной системы выступит совместная '
                    u'деятельность органов власти, научного и предпринимательского сообществ на принципах '
                    u'государственно-частного партнерства')
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(u'I want to христианский break free')
# predict tags and print
model.predict(sentence)
print(sentence.to_tagged_string())