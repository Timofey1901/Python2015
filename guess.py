import random
number = random.randint(1,10)
playernumber = int(input())
if playernumber == number:
    print("WIN")
else:
    print("LOSE")