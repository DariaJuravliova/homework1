n = input('введи номер билетика:')

s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])

if s1 == s2:
    print('поздравляю, у тебя счастливый билетик')
else:
    print('это обычный билетик, в следующий раз тебе повезет')

