def find_unique_string(str):
    """
    Description: If the string has unique character the function will return True otherwise
    False.
    :param str: String input.
    :return: Boolen value.
    Time Complexity: O(c) where c is length of the string passed to the function.
    """
    original_length = len(str)
    remove_duplicate = set()
    for i in range(0, original_length):
        remove_duplicate.add(str[i])
    new_length = len(remove_duplicate)
    if new_length == original_length:
        return True
    else:
        return False


# test case 1

print(find_unique_string("ased34$"))

# test case 2

print(find_unique_string("ased34$12212"))

# test case 3

print(find_unique_string("AWsa"))

# test case 4

print(find_unique_string("  "))
