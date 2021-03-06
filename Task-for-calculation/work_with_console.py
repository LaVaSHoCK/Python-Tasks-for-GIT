import datetime

#----------------print text-----------------
#Вывести на экран текст "Silence is golden".

print("-Silence is golden\n")

#----------------print date and name--------
#Вывести на экран текущее название дня недели,
#название месяца и свое имя. Каждое слово
#должно быть в отдельной строке.

now = datetime.datetime.now()

print (now.strftime("-%A \n-%B \n-DANIL \n"))

#---------------print zerro-----------------
#Вывести на экран пять строк из нулей,
#причем количество нулей в каждой строке
#равно номеру строки.

catch = {1, 2, 3, 4, 5}

for i in catch:
    print("-","0"*i)

#--------------print rectangle--------------
#Вывести на экран прямоугольник, заполненный
#буквами А. Количество строк в прямоугольнике
#равно 5, количество столбцов равно 8.

print ("\n-","A"*5)
print ("-","A"*5)
print ("-","A"*5)
print ("-","A"*5)
print ("-","A"*5)
print ("-","A"*5)
print ("-","A"*5)
print ("-","A"*5,"\n")

#--------------print "W"--------------------
#Вывести на экран букву "W" из символов "*" (звездочка).

print("*     *     *")
print(" *   * *   * ")
print("  * *   * *  ")
print("   *     *   \n")

#--------------print 1+2-4--------------------
#Вывести на экран результат вычисления 1+2−4.

print(1 ," + ", 2, " - ", 4, " = ", 1 + 2 - 4)
