
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

message = ''
for idx in range(len(lst1)-1):
    sub = lst1[idx]
    sub1 = lst1[idx+1]
    if sub == '"':
        if sub1[-1].isdigit():
            # lst1[sub:sub1] = ''.join(lst1[sub:sub1])
            message += f"{sub}"
            continue
    elif sub[-1].isdigit():
        # lst1[sub:sub1] = ''.join(lst1[sub:sub1])
        message += f"{sub}"
        continue
    message += sub
    message += ' '
print(message)