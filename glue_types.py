path_marked = '/home/anna/Desktop/markup/brat_data/marked/marked_train.txt'
path_to_right = "/home/anna/Desktop/markup/brat_data/marked/glued.txt"
path_to_me = "/home/anna/Desktop/markup/brat_data/marked/glued_to_work.txt"
with open(path_marked, 'r') as f:
	with open(path_to_me, "w") as g:
		current_phrase = ["", 0, 0, ""]
		for s in f:
			str = s.split()
			if str[3][1:3] == "B-":
				current_phrase[0] = current_phrase[0].strip()
				if current_phrase[0] != "":
					for punct in [".", ",", ":", ";", "'", "!", "?", "-"]:
						current_phrase[0] = current_phrase[0].replace(" " + punct, punct)
					# g.write(current_phrase[3]+"\t\t"+current_phrase[1]+"\t\t"+current_phrase[2]+"\t\t"+current_phrase[0]+"\n")
					g.write(current_phrase[3]+"\t\t" +current_phrase[0]+"\n")
				current_phrase[0]=str[0]+" "
				current_phrase[1]=str[1]
				current_phrase[2]=str[2]
				# current_phrase[3]=str[3][3:-1]
				current_phrase[3]=str[3][1:-1]
			else:
				current_phrase[0] += str[0] + " "
				current_phrase[2] = str[2]
		# g.write(current_phrase[3] + "\t\t" + current_phrase[1] + "\t\t" + current_phrase[2] + "\t\t" + current_phrase[0]+"\n")
		g.write(current_phrase[3] + "\t\t" + current_phrase[0]+"\n")
		# if