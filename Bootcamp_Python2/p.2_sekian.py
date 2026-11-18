import random

choose_level = int(input("level 1-3:"))

if choose_level == 1:
    max_angka = 10
elif choose_level == 2:
    max_angka = 50
else:
    max_angka == 100


secret_number = random.randint(1, max_angka)
guess = int(input(f"guess the number 1 - (max_angka):"))

while guess != secret_number:
    guess = int(input("your guess"))

    if guess > secret_number:
        print("Too hight")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("correct!")