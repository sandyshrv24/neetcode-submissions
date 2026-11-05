def add_two_numbers() -> int:
    string=input()
    list_of_char=string.split(",")
    int_list=[]
    for i in list_of_char:
        int_list.append(int(i))
    return sum(int_list)    




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
