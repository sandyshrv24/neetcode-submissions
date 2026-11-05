def add_two_numbers() -> int:
    string=input()
    list_of_char=string.split(",")
    int_list=[]
    for i in list_of_char:
        int_list.append(int(i))
    return int_list[0]+int_list[1]    




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
