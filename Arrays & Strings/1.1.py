



def find_unique_string(str):
    original_length = len(str)
    remove_duplicate = set()
    for i in range(0,original_length):
        remove_duplicate.add(str[i])

    new_length = len(remove_duplicate)
    if new_length == original_length:
        return True
    else:
        return False



#test case 1

print(find_unique_string("ased34$"))

#test case 2

print(find_unique_string("ased34$12212"))


#test case 3

print(find_unique_string("AWsa"))

#test case 4

#test case 2

print(find_unique_string("  "))




