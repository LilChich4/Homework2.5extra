import random
def generate_password(n):
    password = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            if n % (i + j) == 0:
                password.append(f"{i}{j}")
    return "".join(password)

n = random.randint(3, 20)
print(f"Первая ячейка: {n}")
print(f"Пароль: {generate_password(n)}")











