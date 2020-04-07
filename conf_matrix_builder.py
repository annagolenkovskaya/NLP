import pymorphy2, numpy, pandas
from pycm import *

morph = pymorphy2.MorphAnalyzer()
names = ['B-ACT', 'I-ACT', 'B-BIN', 'I-BIN', 'B-CMP', 'I-CMP', 'B-QUA', 'I-QUA', 'OUT', 'B-SOC', 'I-SOC', 'B-ECO',
         'I-ECO', 'B-INST', 'I-INST', 'B-MET', 'I-MET']
test = '/home/anna/Desktop/markup/brat_data/marked/train/test.txt'
marked = '/home/anna/Desktop/markup/brat_data/marked/train/marked_train_new_all_altered_with_out_clean.txt'

# test_data = []
# with open(test, 'r') as f:
# 	test_data = f.readlines()
# print(len(test_data), test_data)

# for t in range(len(test_data)):
# 	test_data[t] = test_data[t].replace(' ', '\t')
# print(len(test_data), test_data)
# with open(test, 'w') as f:
# 	f.writelines(test_data)
# raise Exception

matrix = numpy.zeros((9, 9))
test_df = pandas.read_csv(test, sep='\t', header=None)
predicted_df = pandas.read_csv(marked, sep='\t', header=None)
print("len(predicted_df) =", len(predicted_df[0]))
print("len(test_df) =", len(test_df[0]))
predicted_df[0] = predicted_df[0].apply(lambda x: morph.parse(x.lower())[0].normal_form)
# print(type(test_df[1].values))
# for pr in range(len(predicted_df[0])):
# 	print("predicted_df[0][{}] =".format(pr), predicted_df[0][pr])
# 	print("test_df[0][{}] =".format(pr), test_df[0][pr])

cm = ConfusionMatrix(actual_vector=test_df[1].values, predict_vector=predicted_df[1].values)
# print(cm.classes)
print(cm.table)
print(cm)
# for pr in range(len(predicted_df[0])):
	# print("predicted_df[0][{}] =".format(pr), predicted_df[0][pr])
	# print("test_df[0][{}] =".format(t), test_df[0][t])

	# if predicted_df[0][pr] == test_df[0][t]:
	# 	predicted_cutted_words.append(predicted_df[0][pr])
	# 	predicted_cutted_tags.append(predicted_df[1][pr])
	# 	t += 1
	# else:
	# 	pr += 1

# print("predicted_cutted_words =", len(predicted_cutted_words), predicted_cutted_words)
# print("predicted_cutted_tags =", len(predicted_cutted_tags), predicted_cutted_tags)
# print(test_df)
# print(df2)
# df1 = df1.sort_values(by=0)
# df2 = df2.sort_values(by=0)

# conf_mat_dict={}
#
# for label_col in range(len(names)):
#     y_true_label = test_df[:, label_col]
#     y_pred_label = predicted_df[:, label_col]
#     conf_mat_dict[names[label_col]] = confusion_matrix(y_pred=y_pred_label, y_true=y_true_label)


# for label, matrix in conf_mat_dict.items():
#     print("Confusion matrix for label {}:".format(label))
#     print(matrix)
# df = pandas.merge_asof(df1, df2, on=0, suffixes=('_true', '_predicted'), direction='nearest')
# print(len(df))
# for i in range(len(names)):
# 	for j in range(len(names)):
# 		matrix[i][j] = len(df[(df['1_true'] == names[i]) & (df['1_predicted'].apply(lambda x: str(x)[-len(names[j]):]) == names[j])])
# print(matrix)