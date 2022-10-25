import re

isu = 331484 % 5
# мой вариант - 4

test1 = "ГнилОморД"
test2 = "ДокторБумС"
test3 = "ВанХелЬсиНка"
test4 = "123АбрАкаДабра123"
test5 = "Ван хельСинский Округ"
tests = [test1, test2, test3, test4, test5]

print("СПОСОБ С ОДИНАКОВЫМ РАССТОНИЕМ")
for i in tests:
    distance = 0
    overlap = 0
    upper = re.split(r"[A-Я]", i)
    for j in upper:
        if j:
            if distance == len(j):
                overlap += 1
            else:
                distance = len(j)
    if overlap == 1:
        print("Тест", tests.index(i) + 1, "верный")
