my_list = [1,2,3,4,3,4,5,6,4,6,7,8,9,2]

target = 10

for char in my_list:
	if abs(char - 10) in my_list:
		print("{0} and {1}".format(char,abs(char-10)))