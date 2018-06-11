my_list = [1,2,3,4,5,6,4,5,6,7,0,9]
target_value = 15

new_list = list(my_list)


print(my_list)
print(new_list)

for char in my_list:
	if (target_value - char) in new_list:
		print("The pairs are: ##Index :{0} ##Value : {2} and ##Index: {1} ##Value: {3}".format(my_list.index(char),new_list.index((target_value - char)),char,(target_value - char)))
