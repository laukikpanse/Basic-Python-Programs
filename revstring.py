my_string = "hello hello hello hello sir how are you you you how hello"

new_string = my_string.split()

my_dict = dict()


for char in new_string:
	if char in my_dict:
		my_dict[char] += 1
	else:
		my_dict[char] = 1

print(my_dict)

