import re

isu = 331484 % 2
# мой вариант - 2

test1 = "123 ВТ это ИТМО!"
test2 = "123ВТ это важная часть ИТМО!"
test3 = "ВТ самый лучший универ ИТМО ВТ всех ИТМО ВТИТМО"
test4 = "ВТВТ ВТ ИТМО123"
test5 = "ВТ ВТ ВТ ИТМО ИТМО"
tests = [test1, test2, test3, test4, test5]

print("НОРМАЛЬНЫЙ СПОСОБ")
for i in tests:
    temp = re.finditer(r"\bВТ\b( [^ ]+){,4} \bИТМО\b", i)
    for j in temp:
        print("Тест", tests.index(i) + 1, "-", j.group())

print("ТУПОЙ СПОСОБ")
patterns = [r"\bВТ\b\s+\bИТМО\b",
            r"\bВТ\b\s+\w+\s+\bИТМО\b",
            r"\bВТ\b\s+\w+\s+\w+\s+\bИТМО\b",
            r"\bВТ\b\s+\w+\s+\w+\s+\w+\s+\bИТМО\b",
            r"\bВТ\b\s+\w+\s+\w+\s+\w+\s+\w+\s+\bИТМО\b"]

for i in tests:
    for j in patterns:
        if re.findall(j, i):
            result = re.findall(j, i)
            print("Тест", tests.index(i) + 1, "-", result[0])
