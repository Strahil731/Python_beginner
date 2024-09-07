deposit_sum = float(input())
deposit_month = int(input())
year_person = float(input())

interest_price = deposit_sum * (year_person / 100)
interest_price_per_month = interest_price / 12
sum = deposit_sum + deposit_month * interest_price_per_month

print(sum)