import re

isu = 331484 % 5
# мой вариант - 4

test1 = "ааУаааУаааУаа"  # TRUE
test2 = "УуааУаааУ"  # SELECTED WORD IN INTERVAL
test3 = "УааУааааааУ"  # FALSE BY DISTANCE
test4 = "УааУааУааУааУ"  # FALSE BY SELECT
test5 = "ааУаауУааааауУаа"
tests = [test1, test2, test3, test4, test5]

for test in tests:

    distance = 0
    flag = False

    intervals = re.split(r"[A-Я]", test)
    select = re.findall(r"[A-Я]", test)

    if len(select) == 3:
        interval = [intervals[1], intervals[2]]

        for j in interval:
            if j:
                if (select[0].lower() in j) or (select[1].lower() in j) or (select[2].lower() in j):
                    print("Test", tests.index(test) + 1, "SELECTED WORD IN INTERVAL")
                    break
                else:
                    if distance == len(j):
                        print("Test", tests.index(test) + 1, "TRUE")
                        break
                    else:
                        distance = len(j)

                    if flag:
                        print("Test", tests.index(test) + 1, "FALSE BY DISTANCE")
                        break
                    flag = True

    else:
        print("Test", tests.index(test) + 1, "FALSE BY SELECT")
