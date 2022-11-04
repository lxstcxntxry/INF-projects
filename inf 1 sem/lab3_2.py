import re

tests = [
    "ВТ - - - - - ИТМО",  # +
    "ВТ это ! супер база ИТМО",  # +
    "ВТ123 это важная часть ИТМО!",  # -
    "123ВТ это важ-на-я часть ИТМО123",  # -
    ]

tests_re = [
    "ВТ ВТ ИТМО ИТМО",  # 4
    "ВТ ВТ ВТ ВТ ИТМО ИТМО"  # 8
    ]

for test in tests:
    temp = re.sub(r"[^ А-Яа-я0-9_]\s", r"", test)
    res = re.finditer(r"\bВТ\b( [^ ]+){0,4} \bИТМО\b", temp)

    for r in res:
        print("test", tests.index(test) + 1, "-", r.group())

for test in tests_re:
    arr = test.split(" ")
    for i in range(len(arr)):
        resultArr = ""
        for j in range(1, len(arr)):
            if arr[i] == "ВТ" and arr[j] == "ИТМО":
                print("test_re", tests_re.index(test) + 1, "-", " ".join(arr[i:j]), "ИТМО")
