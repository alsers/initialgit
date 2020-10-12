def Luhn(cadnum):
    cardnums = list(str(cadnum))
    cardnums1 = list(str(cadnum))
    cdinum = 0
    for i in range(15):
        if i % 2 == 0:
            number = int(cardnums1[i]) * 2
            if number > 9:
                cardnums1[i] = number % 10 + 1
            else:
                cardnums1[i] = number
        cardnums1[i] = str(cardnums1[i])
        cdinum += int(cardnums1[i])
    if cdinum % 10:
        cardnums[-1] = str(10 - (cdinum % 10))
    else:
        cardnums[-1] = str(0)
    return int(''.join(cardnums))




print(Luhn(4000008449433409))