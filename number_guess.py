import random
limit = int(input('Enter the number limit of range: '))
num = random.randrange(1,limit)
guess = int(input(f'Enter the number between {1, limit}: '))
while num!=guess:
    if guess<num:
        print(f"{guess} is low, enter number again")
        guess = int(input('Enter the number: '))

    elif guess>num:
        print(f"{guess} is high, enter number again")
        guess = int(input('Enter the number: '))

    else:
        break
print(f"WON!! You guessed the number right")


