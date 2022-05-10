
lst = ['в', '-3', 'часа', '14857', 'минут', 'температура', 'воздуха', 'была', '5', 'градусов', 'а', 'воды', '+1']
lst1 = []
for el in lst:
    ind = len(lst1) + 2
    if el[0] == '-' or el[0] == '+' and el[1].isdigit():
        sig = '{:>02}'.format(el[1:])
        el = el[0] + sig
        lst1.extend(['"', el])
        lst1.insert(ind, '"')
        continue
    elif el[0].isdigit():
        el = '{:>02}'.format(el)
        lst1.extend(['"', el])
        lst1.insert(ind, '"')
        continue
    lst1.append(el)
print(lst1)
print('')

message = sub for sub in range(len(lst1):
    if lst1[lst1.index(sub)] = '"':
        if lst1[lst1.index(sub)+1][-1].isdigit():
            print(lst1.index(sub))
            lst1[lst1.index(sub):(lst1.index(sub) + 1)] = [''.join(lst1[lst1.index(sub):(lst1.index(sub) + 1)])]
            message += sub
            continue
    elif lst1[lst1.index(sub)][-1].isdigit():
        lst1[lst1.index(sub):(lst1.index(sub) + 1)] = [''.join(lst1[lst1.index(sub):(lst1.index(sub) + 1)])]
        message += sub
        continue
    message += sub
    message += " "
print(message)