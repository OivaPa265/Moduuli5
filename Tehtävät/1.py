import random

kysymys = int(input("kuinka monta noppaa"))
summa=0
for noppa_1 in range (kysymys):

    luku = random.randint(1, 6)
    print (f"noppaa {noppa_1+1} and luku {summa}")

    summa += luku

    print(f"Noppien summa on{summa} ")
