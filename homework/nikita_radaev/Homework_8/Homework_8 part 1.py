import random

bonus = random.choice([True, False])
salary = int(input(""))
if bonus:
    addition = int(random.random() * 100)
    print(f"${salary + addition}")
else:
    print(f"${salary}")
