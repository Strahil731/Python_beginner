# Пилешко меню –  10.35 лв.
# Меню с риба – 12.40 лв.
# Вегетарианско меню  – 8.15 лв.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

number_chicken_menus = int(input())
number_menus_with_fish = int(input())
number_vegetables_menus = int(input())

price_from_chicken_menus = number_chicken_menus * 10.35
price_from_menus_with_fish = number_menus_with_fish * 12.40
price_from_vegetables_menus = number_vegetables_menus * 8.15

all_price = price_from_chicken_menus + price_from_menus_with_fish + price_from_vegetables_menus
price_with_decert = all_price * 0.20

sum = all_price + price_with_decert + 2.50

print(sum)