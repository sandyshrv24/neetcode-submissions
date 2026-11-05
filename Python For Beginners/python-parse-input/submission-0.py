from typing import List

def read_integers() -> List[int]:
    string=input()
    my_list = string.split(",")
    my_int_list =[]
    for i in my_list:
        i=int(i)
        my_int_list.append(i)
    return my_int_list    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
