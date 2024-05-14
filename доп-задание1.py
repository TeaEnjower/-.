def reverse_dict(dict_items_in):
    dict_out = dict()
    for key, value in dict_items_in:
        dict_out[value] = key
    return dict_out

slovar = {1: 'Kirill', 2: 'i', 3: 'Mefodiy'}
print(reverse_dict(slovar.items()))


# or:

print({value: key for key, value in slovar.items()})