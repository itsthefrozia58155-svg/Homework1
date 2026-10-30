import random

number = random.randint(1, 10)
attempts = 3

print("Вгадай  число від 1 до 10. У вас є 3 спроби.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}: Введіть ваше число: "))

    if guess == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess > number:
        print("<")
    else:
        print(">")
else:
    print(f"Ви використали всі спроби. Я загадав число: {number}")