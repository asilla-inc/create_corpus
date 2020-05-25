import random

for i in range(650):
    integer = random.randint(1,99)
    floating = random.randint(1,9)

    text = f"{integer}.{floating}\n"
    with open('numbers.txt', 'a') as file:
        file.writelines(text)