'''
1
dolbaeb = int(input('Введите свой возраст: '))
if dolbaeb > 14:
    print("Добро пожаловать!")
elif dolbaeb < 14:
    print("Вам ещё рано!")
else:
    print("Вам 14 лет! Поздравляю!")
2
piska = 'secret'
popa = input('Введите пароль: ')
if piska == popa:
    print("Доступ разрешен!")
else:
    print("Неверный пароль!")
3
kys = input("Введите символ: ")

if kys.isdigit():
    print("Это цифра!")
elif kys.isalpha():
    print("Это буква!")
else:
    print("Это не цифра и не буква!")
4
sraka = int(input('Введите стоимость товара: '))
if sraka > 1000:
    noga = 0.1
elif sraka > 500:
    noga = 0.05
else:
    noga = 0
konechnaya_sraka = sraka - (sraka * noga)
print('Конечная стоимость товара: ', konechnaya_sraka)
5
for sigma in range(5):
    a = int(input())
print(a + a + a + a + a)
6
pupa = int(input())

factorial = 1
for jopa in range(1, pupa + 1):
    factorial *= jopa

print(factorial)
7
terka = int(input("Введите число: "))

if terka <= 1:
    print("Число не простое")
else:
    prostaya_terka = True
    for i in range(2, int(terka ** 0.5) + 1):
        if terka % i == 0:
            prostaya_terka = False
            break

    if prostaya_terka:
        print("Число простое")
    else:
        print("Число не простое")
8
westi = input()

kolvo_glasnuh = 0

for bukva in westi:
    bukva = bukva.lower()

    if bukva in ['a', 'e', 'i', 'o', 'u']:

        kolvo_glasnuh += 1

print(kolvo_glasnuh)'''
