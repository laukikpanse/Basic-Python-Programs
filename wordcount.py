my_string = input("ENter some String: ")


my_dict = dict()

new_string = my_string.split()
i = 1

for char in new_string:
	if char in my_dict:
		i = my_dict[char]
		my_dict[char] = i+1
		pass
	else:
		i = 1
		my_dict[char] = i

print(my_dict)