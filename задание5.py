def data_base(operation, data):
    global school
    if operation == 1:
        if data['класс'] in school.keys():
            school[data['класс']]['количество'] += data['количество']
        else:
            print('Такого класса нет')
            print(school)
            return
    elif operation == 2:
        school[data['класс']] = {'количество': data['количество']}
    elif operation == 3:
        curr_form = data['класс']
        curr_num = school[curr_form]['количество']
        if curr_form not in school:
            print('Такого класса и так не было')
            print(school)
            return
        del school[curr_form]
        for i in set(curr_form):
            if not i.isdigit():
                curr_form = curr_form.replace(i, '')
        similar_forms = []
        for i in school.keys():
            if i.startswith(curr_form):
                similar_forms.append(i)
        if not similar_forms:
            print(f'Был создан класс {curr_form}. Так как все остальные классы этого года расформировались')
            school[curr_form] = {'количество': curr_num}
            print(school)
            return
        refactoring = curr_num // len(similar_forms)
        for i in similar_forms[:-1]:
            school[i]['количество'] += refactoring
            curr_num -= refactoring
        school[similar_forms[-1]]['количество'] += curr_num
    elif operation == 4:
        curr_sum = 0
        classes = []
        for key, info in school.items():
            classes.append(key)
            curr_sum += info['количество'] 
        print(f'На данный момент в школе учатся {curr_sum} учеников. Классы: ', *classes, sep='\n')
        return
    print(school)

school = {'7а': {'количество': 10}}
print(school)
data_base(1, {'класс': '7а', 'количество': -2})
data_base(2, {'класс': '8б', 'количество': 19})
data_base(3, {'класс': '7а'})
print('---')
data_base(4, None)