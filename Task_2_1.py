# 1. Выяснить тип результата следующих выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
# Техническое задание:
#
# Вывести на экран тип выражения и отдельно проверить является ли полученный тип целым числом.

var1 = 15 * 3
var2 = 15 / 3
var3 = 15 // 2
var4 = 15 ** 2

if isinstance ( var1 , int ):
    print( type ( var1 ), True)
else: print( type ( var1 ), False)

if isinstance ( var2 , int ):
    print( type ( var2 ), True)
else: print( type ( var2 ), False)

if isinstance ( var3 , int ):
    print( type ( var3 ), True)
else: print( type ( var3 ), False)

if isinstance ( var4 , int ):
    print( type ( var4 ), True)
else: print( type ( var4 ), False)