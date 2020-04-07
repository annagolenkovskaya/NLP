from glob import glob
from flair.data import Sentence
from flair.models import SequenceTagger
import pymorphy2
from copy import copy

morph = pymorphy2.MorphAnalyzer()


def to_normal_forms(sentence_input, morph=morph):
	for punct in [".", ",", ":", ";", "'", "!", "?", "-"]:
		sentence_input.replace(punct, " "+punct)
	sentence_input.replace("\" ", " \" ")
	sentence_input.replace(" \"", " \" ")
	sentence_input.replace("\' ", " \' ")
	sentence_input.replace(" \'", " \' ")
	sentence = copy(sentence_input)
	new_sentenece = sentence.lower().split()
	for i in range(len(new_sentenece)):
		new_sentenece[i] = morph.parse(new_sentenece[i])[0].normal_form
	s=""
	for word in new_sentenece:
		s+=word+" "
	s = s.strip()
	return s, sentence_input


def back_to_initial_form(tagged_string, initial_form, starting_symbol_number):
	answer = []
	splited_tagged_string = tagged_string.split()
	splited_initial_form = initial_form.split()
	current_start_symbol_number = starting_symbol_number
	for i in range(len(splited_initial_form)):
		current_end_symbol_number = current_start_symbol_number + len(splited_initial_form[i])
		if 	splited_initial_form[i] in [".", ",", ":", ";", "'", "!", "?", "-", "\"", "\'"]:
			current_end_symbol_number -=1
		# if splited_tagged_string[2*i+1] != "<OUT>":
		answer.append([splited_initial_form[i], current_start_symbol_number, current_end_symbol_number, splited_tagged_string[2*i+1]])
		current_start_symbol_number = current_end_symbol_number+1
	return answer



path = glob('/home/anna/Desktop/markup/brat_data/train/*.txt')
path_marked = '/home/anna/Desktop/markup/brat_data/marked/marked_train_new.txt'
path_marked_not_full = '/home/anna/Desktop/markup/brat_data/marked/train/marked_train_new_all_altered_with_out.txt'
path_test = '/home/anna/Desktop/markup/brat_data/marked/train/test.txt'
test_data = []
# for d in path:
# 	with open(d, 'r') as f:
# 		test_data.append(f.read().splitlines())

with open(path_test, 'r') as f:
	test_data.append(f.read().splitlines())

test_data = sum(test_data, [])

model = SequenceTagger.load('/home/anna/Desktop/markup/brat_data/marked/train/model/best-model.pt')

starting_symbol_number=0
with open(path_marked_not_full, 'w') as f:
	for s in test_data:
		length = len(s)
		if length > 0:
			normal_forms, inital_forms = to_normal_forms(s)
			sentence = Sentence(normal_forms)
			model.predict(sentence)
			tagged_string = sentence.to_tagged_string()
			answer = back_to_initial_form(tagged_string, inital_forms, starting_symbol_number)
			for x in answer:
				# f.write(x[0]+" "+str(x[1])+" "+str(x[2])+" "+x[3]+"\n")
				f.write(x[0]+"\t" + x[3][1:-1]+"\n")
			starting_symbol_number += length