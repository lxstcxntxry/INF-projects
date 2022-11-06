Fstr = str(input())

S1 = (int(Fstr[0]) + int(Fstr[2]) + int(Fstr[4]) + int(Fstr[6])) % 2
S2 = (int(Fstr[1]) + int(Fstr[2]) + int(Fstr[5]) + int(Fstr[6])) % 2
S3 = (int(Fstr[3]) + int(Fstr[4]) + int(Fstr[5]) + int(Fstr[6])) % 2

iSum = int(S3) * 4 + int(S2) * 2 + int(S1)

if iSum != 0:
    if int(Fstr[iSum - 1]) == 0:
        Tstr = Fstr[:(iSum - 1)] + '1' + Fstr[iSum:]
    else:
        Tstr = Fstr[:(iSum - 1)] + '0' + Fstr[iSum:]
    print("ошибка в бите ", iSum)
    print("правильная строка ", Tstr)
else:
    Tstr = Fstr[2] + Fstr[4] + Fstr[5] + Fstr[6]
    print("нет ошибок:", Tstr)
