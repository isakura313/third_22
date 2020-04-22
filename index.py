import random

amountOfBullets = input("А сколько зарядить? ")
aob = int(amountOfBullets)
baraban = [0, 0, 0, 0, 0, 0]

for i in range(aob):
    baraban[i] = 1

print(baraban, "выглядит сейчас вот так")

howMuch = input("Сколько раз крутить? ")
hm = int(howMuch)
for i in range(hm):
    random.shuffle(baraban)
    if baraban[0] == 1:
        print("оглушительный выстрел!\a")
    else:
        print("щелк")
