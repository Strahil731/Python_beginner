film_budget = float(input())
number_of_statist = int(input())
price_clothing_for_one_statist = float(input())

decor_price = film_budget * 0.10
price_from_clothing = number_of_statist * price_clothing_for_one_statist

if number_of_statist >= 150:
    price_from_clothing -= price_from_clothing * 0.10
sum = price_from_clothing + decor_price

if sum > film_budget:
    price_discount = sum - film_budget
    print("Not enough money!")
    print(f"Wingard needs {price_discount:.2f} leva more.")
else:
    price_after_film = film_budget - sum
    print("Action!")
    print(f"Wingard starts filming with {price_after_film:.2f} leva left.")