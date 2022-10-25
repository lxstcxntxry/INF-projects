import re

isu = 331484
eyes = [":", ";", "X", "8", "=", "["]
nose = ["-", "<", "-{", "<{"]
mouth = ["(", ")", "O", "|", "\\", "/", "P"]

mySmile = str(eyes[331484 % 6]) + str(nose[331484 % 4]) + str(mouth[331484 % 7])
# мой смайл - "X-P"
test1 = "X-P:<(;<OX-P123X-)X-("  # 2
test2 = "12345X-P12345"  # 1
test3 = "P-X-X-X-P"  # 1
test4 = "X9-999X-X-X"
test5 = "X-PP-XX-XX-PP-XX-PX-PX-P"  # 5
tests = [test1, test2, test3, test4, test5]

for i in tests:
    print("Тест", tests.index(i) + 1, "-", len(re.findall(mySmile, i)), "моих смайлика(-ов)")
