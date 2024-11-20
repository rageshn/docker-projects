from random import randint

min_num = int(input("Enter minimum number: "))
max_num = int(input("enter maximum number: "))

if min_num > max_num:
    print("Invalid input")
else:
    rnd_num = randint(min_num, max_num)
    print(rnd_num)