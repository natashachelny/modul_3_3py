def print_params(a=1, b="строка", c=True):
    print(a, b, c)
print_params(9, "Ilona")
print_params(None, [8,6,5],"Я всё смогу!" )
print_params(1000)
print_params()

print_params (b = 25)
print_params(c = [1,2,3])

values_list = ["Наталья", 27887, [5, 6, 7]]
values_dict = {"a": [5, 6, 7], "b": "Наталья", "c": 27887}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [27.88, "Фортуна"]
print_params(*values_list_2, 42)

