import random

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'



# Инициализация переменных
krestic = "Крестик"
nolik = "Нолик"

pole_igrovoe = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]

x = ["1", "2", "3"]

g = ["1", "2", "3"]

counter_0 = 0
turn = "player"

# Логика выбора команды перед началом игры
while True:
    comands = input("Имеющиеся команды:\n1.Крестик\n2.Нолик\n\nВведите команду: ")
    if comands == nolik or comands == krestic:
        print("Вы молодцы, правильный ввод!".upper())
        break
    else:
        print("Ввод неправильный!".upper())

# Логика проверки, кто будет ходить первым
if turn == "player":
    print(YELLOW + "Ваш ход" + RESET)

# Логика позиций для крестиков и ноликов на игровом поле
while True:
    print(UNDERLINE + BLUE + BOLD + "КРЕСТИКИ-НОЛИКИ".upper() + RESET)
    print("-----------------")

    # Логика счётчика ходов в течение игры
    counter_0 += 1
    print(CYAN + f"Количество ходов за раунд: {counter_0}".upper() + RESET)
    print("-----------------")

    print(f"   {x[0]} {x[1]} {x[2]}")

    # Логика проверки ввода данных
    for j, i in enumerate(pole_igrovoe):
        print(f"{g[j]}  {' '.join(i)}")
    print("-----------------")

    if turn == "player":
        try:
            cords = int(input(GREEN + "Значение для ввода (пример):\n2 - горизонталь\n3 - вертикаль\nВведите координату (в виде целого числа без доп.символов): " + RESET))
            print("-----------------\n")
            if cords < 11 or cords > 33:
                print(RED + "Тип ответа - неподходящая длина строки!".upper() + RESET)
                print(RED + "Попробуйте снова!\n".upper() + RESET)
                continue

            row = (cords // 10) - 1
            col = (cords % 10) - 1

            # Проверка занятости ячейки
            if pole_igrovoe[row][col] != "-":
                print(RED + "Данная ячейка уже задана!".upper() + RESET)
                print(RED + "Попробуйте ввести другие значение!" + RESET)
                continue

            # Логика выставления ноликов и крестиков на игровом поле с учётом выбранной команды
            if comands == krestic:
                pole_igrovoe[row][col] = "X"
            elif comands == nolik:
                pole_igrovoe[row][col] = "O"

            turn = "ai"

        except ValueError:
            print("Тип ответа - некорректный!".upper())
            print("Попробуйте снова!\n".upper())

    else:
        print(MAGENTA + "Ход компьютера" + RESET)
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if pole_igrovoe[row][col] == "-":
                if comands == krestic:
                    pole_igrovoe[row][col] = "O"
                elif comands == nolik:
                    pole_igrovoe[row][col] = "X"
                break

        turn = "player"

    # Проверка на победу или ничью
    if all([pole_igrovoe[0][0] == "X",
            pole_igrovoe[1][0] == "X",
            pole_igrovoe[2][0] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][0] == "X",
            pole_igrovoe[0][1] == "X",
            pole_igrovoe[0][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[1][0] == "X",
            pole_igrovoe[1][1] == "X",
            pole_igrovoe[1][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[2][0] == "X",
            pole_igrovoe[2][1] == "X",
            pole_igrovoe[2][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][1] == "X",
            pole_igrovoe[1][1] == "X",
            pole_igrovoe[2][1] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][2] == "X",
            pole_igrovoe[1][2] == "X",
            pole_igrovoe[2][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][0] == "X",
            pole_igrovoe[1][1] == "X",
            pole_igrovoe[2][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[2][0] == "X",
            pole_igrovoe[1][1] == "X",
            pole_igrovoe[0][2] == "X",
            comands == krestic]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][0] == "O",
            pole_igrovoe[1][0] == "O",
            pole_igrovoe[2][0] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][0] == "O",
            pole_igrovoe[0][1] == "O",
            pole_igrovoe[0][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[1][0] == "O",
            pole_igrovoe[1][1] == "O",
            pole_igrovoe[1][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[2][0] == "O",
            pole_igrovoe[2][1] == "O",
            pole_igrovoe[2][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][1] == "O",
            pole_igrovoe[1][1] == "O",
            pole_igrovoe[2][1] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][2] == "O",
            pole_igrovoe[1][2] == "O",
            pole_igrovoe[2][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[0][0] == "O",
            pole_igrovoe[1][1] == "O",
            pole_igrovoe[2][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break
    elif all([pole_igrovoe[2][0] == "O",
            pole_igrovoe[1][1] == "O",
            pole_igrovoe[0][2] == "O",
            comands == nolik]):
        print("Победа!".upper())
        break

    if all([cell != "-" for row in pole_igrovoe for cell in row]):
        print(UNDERLINE + BOLD + RED + "Поражение!".upper() + RESET)
        break

