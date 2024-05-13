def remove_duplicates_and_spaces(input_string):
    result = ''
    for char in input_string:
        if char not in result:
            result += char
    return result

user_input = input("Введите строку: ")
print(remove_duplicates_and_spaces(user_input))