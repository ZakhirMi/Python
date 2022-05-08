

lst = ['в', '-33', 'часа', '14857', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов', 'а', 'воды', '+1']
for el in lst:
    dig = el.split('+' or '-')
    print(dig)
    # if el.index(-1).isdigit():
    #     print(el)