# 3. Реализовать склонение слова «процент» во фразе «N процентов».

counter = 0
while counter <= 101:
    if counter==1 or counter==101:
        print (counter, "процент")
    elif 2 <= counter <= 4:
        print (counter, "процента")
    else: print(counter, "процентов")
    counter += 1
