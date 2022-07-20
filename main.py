from colorama import init
from colorama import Fore
init()

print(Fore.LIGHTBLUE_EX)
print("Новый калькулятор с усовершенствованным дизайном!!")

print(Fore.LIGHTGREEN_EX)
f = input("Введите первое число: ")
z = input("Введите знак( +; -; *; / ): ")
s = input("Теперь введите второе число: ")

rez = 0

print(Fore.LIGHTCYAN_EX)
if z == "+":
    rez = int(f) + int(s)
    print(f"{rez} - результат.")
elif z == "-":
    rez = int(f) - int(s)
    print(f"{rez} - результат.")
elif z == "*":
    rez = int(f) * int(s)
    print(f"{rez} - результат.")
elif z == "/":
    rez = int(f) / int(s)
    print(f"{rez} - результат.")
else:
    print(Fore.LIGHTRED_EX)
    print("Введена неверная команда")

print(Fore.LIGHTMAGENTA_EX)
print("Спасибо за работу со мной!")