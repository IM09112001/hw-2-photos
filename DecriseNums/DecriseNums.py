#Программа считывает три числа с плавающей запятой и печатает их в порядке убывания. 
#Использование списков с их стандартной функцией sort() в этом задании не допускается.
#Buble sort
from array import*
decriseNum=[0]*3

for i in range(3):
    decriseNum[i]=float(input("Введите цифры:"))
print("Сортировка по убыванию:")
for i in range(3):
   for j in range(len(decriseNum)-1):
       if decriseNum[j]<decriseNum[j+1]:
           wrap=decriseNum[j]
           decriseNum[j]=decriseNum[j+1]
           decriseNum[j+1]=wrap
for i in range(3):
    print(decriseNum[i])    

