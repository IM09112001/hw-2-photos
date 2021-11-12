#Вам даётся текущее время (часы и минуты) и значение дельты(разницы) в часах(может быть любым дробным числом - float).
#Вам необходимо вывести время в дельта-часах от текущего времени в виде единой строки в формате ЧЧ:ММ.

import math
hour=int(input("Введите время: "))
min=int(input("Введите минуты: "))
delta=float(input("Введите разницу во времени: "))
d1=math.floor(delta)
minD=(delta-d1)*60
if minD/minD>1:   minD+=1
if hour>=24 or hour<0:
     print("Введите часы в диапазоне [0; 24)!")
       
elif min>=60 or min<0:
         print("Введите минуты в диапазоне [0; 60)!")
else:   
    
    if delta>=0:
      if minD!=0:
        min+=minD
        if min>=60:
            while min//60!=0 : 
                min//=60
                hour+=1
    if delta<0:
       if minD!=0:
        min-=minD
        if min<0:
            while min>=0 : 
                min//=60
                hour-=1
    if d1>24 or d1<-24:
            while d1//24!=0 : d1//=24    
    if d1<0:
        d1+=24
    if hour+d1<10 and hour+d1>0: 
            if min<10 and min>0: print(f"Временная разница: 0",hour+d1,":0",math.floor(min))
            else: print(f"Временная разница: 0",hour+d1,":",math.floor(min));
            
    elif min<10: print(f"Временная разница: ",hour+d1,":0",math.floor(min))
    else: print(f"Временная разница: ",hour+d1,":",math.floor(min))
  
