import random 

wyborliter = int(input("Jaką długość słów wybierasz? "))
if wyborliter == 4:
    print(random.choice(open('4litery.txt', 'r').readlines()).strip())
elif wyborliter == 5:
    print(random.choice(open('5liter.txt', 'r').readlines()).strip())
elif wyborliter == 6:
    print(random.choice(open('6liter.txt', 'r').readlines()).strip())
else:
    print("Niestety nie mamy do wyboru słów o wybranej przez ciebie długości :(")
