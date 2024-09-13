# Пъзел - 2.60 лв.
# Говореща кукла - 3 лв.
# Плюшено мече - 4.10 лв.
# Миньон - 8.20 лв.
# Камионче - 2 лв

discount = 0
rent_money = 0

holiday_price = float(input())
number_puzzle = int(input())
number_speak_dolls = int(input())
number_teddy_bear = int(input())
number_minions = int(input())
number_trucks = int(input())

sum = number_puzzle * 2.60 + number_speak_dolls * 3 + number_teddy_bear * 4.10 + number_minions * 8.20 + number_trucks * 2.00
all_toy = number_puzzle + number_speak_dolls + number_teddy_bear + number_minions + number_trucks

if all_toy >= 50:
    discount = sum * 0.25
    sum -= discount

rent_money = sum * 0.10
sum -= rent_money

if sum >= holiday_price:
    sum -= holiday_price
    print(f"Yes! {sum:.2f} lv left.")
else:
    holiday_price -= sum
    print(f"Not enough money! {holiday_price:.2f} lv needed.")