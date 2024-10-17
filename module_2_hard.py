def ancient_cipher(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)

    return result


for number in range(3, 21):
    print(f"{number} - {ancient_cipher(number)}")
