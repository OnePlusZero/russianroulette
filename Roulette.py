import random
import os
import time


print("Хватит ли у вас смелости сыграть в игру рулетка?")
r = input("да (1) /нет (2)? ")
if  r == "1":
    while True:
        os.system('cls')
        a = int(input("вставь патрон в любую из 6 камор барабана (число 1-6):  "))
        b = random.randint(1,6)
        if a==b:
            print("вы застрелились, патрон был в" ,b, "каморе")
            time.sleep(3)    
            os.system('cls')
            
        else:
            os.system('cls')
            print("вы выжили, патрон был в" ,b, "каморе")
            time.sleep(3)
            os.system('cls')
            
else:
    os.system('cls')
    print("Фу... Ссыкло!")
    time.sleep(3)
    