immutable_var = 1, 2, 'banana', 2
print(immutable_var)
#immutable_var[0] = 200 # Нельзя изменить
#print(immutable_var.__sizeof__()) # Занимает меньше объем памяти
mutable_list_ = ["apple", "banana", "coconut"]
mutable_list_[2] = 200
print(mutable_list_)