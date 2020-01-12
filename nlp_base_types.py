# The sentence objects holds a sentence that we may want to embed or tag
from flair.data import Sentence, segtok_tokenizer

# Make a sentence object by parsing a whitespace tokenized string
sentence = Sentence('The grass is green .', use_tokenizer=segtok_tokenizer)

# Print the object to see what's in there
# print(sentence)

# using the token id
# print(sentence.get_token(4))
# using the index itself
# print(sentence[3])

# for token in sentence:
# 	print(token)

# add a tag to a word in the sentence
sentence[3].add_tag('ner', 'color')

# print the sentence with all tags of this type
# print(sentence.to_tagged_string())

# get token 3 in the sentence
token = sentence[3]

# get the 'ner' tag of the token
tag = token.get_tag('ner')

# print token
# print(f'"{token}" is tagged as "{tag.value}" with confidence score "{tag.score}"')

sentence = Sentence('France is the current world cup winner.')

# add a label to a sentence
sentence.add_label('sports')

# a sentence can also belong to multiple classes
sentence.add_labels(['sports', 'world cup'])

# you can also set the labels while initializing the sentence
sentence = Sentence('France is the current world cup winner.', labels=['sports', 'world cup'])

print(sentence)
for label in sentence.labels:
	print(label)