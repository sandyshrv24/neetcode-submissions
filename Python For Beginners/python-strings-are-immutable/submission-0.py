def remove_fourth_character(word: str) -> str:
    first_off=word[:3]
    last_off=word[4:]
    return first_off+last_off


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
