def ancient_cipher(n):
    result = ""
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if n % (i + j) == 0:
                result += f"{i}{j}"
    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print("Нужный пароль:", ancient_cipher(n))
else:
    print("Число вне допустимого диапазона.")
