import re

test1 = "ааУаааУаааУаа"
test2 = "ИfffИfffИ"
test3 = "УааУааааааУ"
test4 = "УааУааУааУааУ"
test5 = "ааУаауУааааауУаа"
tests = [test1, test2, test3, test4, test5]

for test in tests:
    distance = 0
    flag = False
    intervals = re.split(r"[A-ZА-Я]", test)
    select = re.findall(r"[A-ZА-Я]", test)

    if len(select) == 3:
        interval = [intervals[1], intervals[2]]
        for j in interval:
            if j:
                if (select[0].lower() in j) or (select[1].lower() in j) or (select[2].lower() in j):
                    print("Test", tests.index(test) + 1, "ошибка: Буквы в интервале")
                    break
                else:
                    if distance == len(j):
                        print("Test", tests.index(test) + 1, "+")
                        break
                    else:
                        distance = len(j)
                    if flag:
                        print("Test", tests.index(test) + 1, "ошибка: Длина промежутков !=")
                        break
                    flag = True
    else:
        print("Test", tests.index(test) + 1, "ошибка: Выбрано много")
