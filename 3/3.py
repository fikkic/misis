kys = input("Введите символ: ")

if kys.isdigit():
    print("Это цифра!")
elif kys.isalpha():
    print("Это буква!")
else:
    print("Это не цифра и не буква!")
