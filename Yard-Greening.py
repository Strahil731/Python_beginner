squart_meters_that_will_be_landscaped = float(input())

all_landscaped_meter_price = squart_meters_that_will_be_landscaped * 7.61
discount = all_landscaped_meter_price * 0.18
price_after_discount = all_landscaped_meter_price - discount

print(f"The final price is: {price_after_discount} lv.")
print(f"The discount is: {discount} lv.")
