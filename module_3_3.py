def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(1, 2 ,3)
print_params('еще одна строка',2)
print_params(c=2)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1.3, 'Hello', True]
values_dict = {'a': 10, 'b': 'cat', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [13.13, "Alice"]
print_params(*values_list_2, 42)