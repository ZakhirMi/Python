# 3. Реализовать склонение слова «процент» во фразе «N процентов».
# Усложнение:
#
# Сделайте эту же задачу для интервала от 1 до 200. Подумайте над тем почему такая задача - усложненная? В чем сложность?

counter = 0
while counter <= 101:
    if counter==1 or counter==101:
        print (counter, "процент")
    elif 2 <= counter <= 4:
        print (counter, "процента")
    else: print(counter, "процентов")
    counter += 1
