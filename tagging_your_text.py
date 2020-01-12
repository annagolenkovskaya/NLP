from flair.models import SequenceTagger
from flair.data import Sentence

tagger = SequenceTagger.load('ner')

sentence = Sentence('George Washington went to Washington .')

# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
# print(sentence.to_tagged_string())

# for entity in sentence.get_spans('ner'):
# 	print(entity)

# print(sentence.to_dict(tag_type='ner'))

# load model
tagger = SequenceTagger.load('de-ner')

# make German sentence
sentence = Sentence('George Washington ging nach Washington .')

# predict NER tags
tagger.predict(sentence)

# print sentence with predicted tags
# print(sentence.to_tagged_string())

# load model
tagger = SequenceTagger.load('multi-pos')

# text with English and German sentences
sentence = Sentence('Джордж Вашингтон приехал в Вашингтон .')

# predict PoS tags
tagger.predict(sentence)

# print sentence with predicted tags
# print(sentence.to_tagged_string())

# load model
tagger = SequenceTagger.load('frame')

# make English sentence
sentence_1 = Sentence('George returned to Berlin to return his hat .')
sentence_2 = Sentence('He had a look at different hats .')

# predict NER tags
tagger.predict(sentence_1)
tagger.predict(sentence_2)

# print sentence with predicted tags
# print(sentence_1.to_tagged_string())
# print(sentence_2.to_tagged_string())

# your text of many sentences
text = "This is a sentence. This is another sentence. I love Moscow."

# use a library to split into sentences
from segtok.segmenter import split_single

sentences = [Sentence(sent, use_tokenizer=True) for sent in split_single(text)]

# predict tags for list of sentences
tagger: SequenceTagger = SequenceTagger.load('ner')
# print(tagger.predict(sentences))

from flair.models import TextClassifier

classifier = TextClassifier.load('en-sentiment')

sentence = Sentence('This film hurts. It is so bad that I am confused.')

# predict NER tags
classifier.predict(sentence)

# print sentence with predicted labels
print(sentence.labels)