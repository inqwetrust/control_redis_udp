f = open('text_list.txt', 'r')
text_list = [t.replace("\n", "") for t in f.readlines()]
text_list = text_list * 200
f.close()

print(text_list)