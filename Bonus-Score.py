number = int(input())
bonus_point = 0

if number <= 100:
    bonus_point = 5

    if number % 10 == 5:
        bonus_point += 2
    elif number % 2 == 0:
        bonus_point += 1
elif number > 100 and number <= 1000:
    bonus_point = number * 0.20

    if number % 10 == 5:
        bonus_point += 2
    elif number % 2 == 0:
        bonus_point += 1
elif number > 1000:
    bonus_point = number * 0.10

    if number % 10 == 5:
        bonus_point += 2
    elif number % 2 == 0:
        bonus_point += 1

number += bonus_point

print(bonus_point)
print(number)