# make an empty character dictionary
from flair.data import Dictionary
char_dictionary: Dictionary = Dictionary()

# counter object
import collections
counter = collections.Counter()

processed = 0

import glob
files = glob.glob('/home/anna/Desktop/markup/learning/*.*')

print(files)
for file in files:
	print(file)

	with open(file, 'r', encoding='utf-8') as f:
		tokens = 0
		for line in f:

			processed += 1
			chars = list(line)
			tokens += len(chars)

			# Add chars to the dictionary
			counter.update(chars)

			# comment this line in to speed things up (if the corpus is too large)
			# if tokens > 50000000: break

	# break

total_count = 0
for letter, count in counter.most_common():
	total_count += count

print(total_count)
print(processed)

sum = 0
idx = 0
for letter, count in counter.most_common():
	sum += count
	percentile = (sum / total_count)

	# comment this line in to use only top X percentile of chars, otherwise filter later
	# if percentile < 0.00001: break

	char_dictionary.add_item(letter)
	idx += 1
	print('%d\t%s\t%7d\t%7d\t%f' % (idx, letter, count, sum, percentile))

print(char_dictionary.idx2item)

import pickle
with open('/home/anna/Desktop/markup/learning/dictionary/dict', 'wb') as f:
	mappings = {'idx2item': char_dictionary.idx2item, 'item2idx': char_dictionary.item2idx}
	pickle.dump(mappings, f)