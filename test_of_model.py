from flair.data import Sentence
from flair.models import SequenceTagger
import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def to_normal_forms(sentence, morph=morph):
	for punct in [".", ",", ":", ";", "'", "!", "?", "-"]:
		sentence.replace(punct, " "+punct)
	sentence.replace("\" ", " \" ")
	sentence.replace(" \"", " \" ")
	sentence.replace("\' ", " \' ")
	sentence.replace(" \'", " \' ")
	new_sentenece = sentence.lower().split()
	for i in range(len(new_sentenece)):
		new_sentenece[i] = morph.parse(new_sentenece[i])[0].normal_form
	s=""
	for word in new_sentenece:
		s+=word+" "
	s = s.strip()
	return s


# load the model you trained
model = SequenceTagger.load('/home/anna/Desktop/markup/brat_data/marked/train/model/best-model.pt')

# create example sentence
sentence = Sentence(to_normal_forms(u'достижения указанной цели.'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'формирования у жителей Республики Коми толерантного сознания и поведения ;'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'содействие укреплению правопорядка и общественной безопасности ;'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'профилактика безнадзорности и правонарушений несовершеннолетних ;'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'создание системы социальной реабилитации несовершеннолетних , освобожденных из мест лишения свободы и осужденных к мерам наказания , не связанным с лишением свободы ;'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'социальной поддержки детей и подростков , находящихся в трудной жизненной ситуации '))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'повышение эффективности борьбы с незаконным оборотом алкогольной и спирто  содержащей продукции ;'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'обеспечение участия общественных организаций , населения в превентивных мерах , направленных на '))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms(u'снижение преступности и охрану общественного порядка . '))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms('Модернизация системы патриотического воспитания.'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms('объем налоговых и неналоговых доходов составил 49,8 млрд. рублей'))
model.predict(sentence)
print(sentence.to_tagged_string())
sentence = Sentence(to_normal_forms('В результате объем  доходов составил 105,7% к плану года'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms('Подготовка граждан к военной службе'))
model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence(to_normal_forms('Налоговых доходов мобилизовано 46,9 млрд.'))
model.predict(sentence)
print(sentence.to_tagged_string())
