# Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка


price_from_one_year = int(input())

price_from_shoes = price_from_one_year - (price_from_one_year * 0.40)
price_from_uniform = price_from_shoes - (price_from_shoes * 0.20)
price_from_ball = price_from_uniform / 4
price_from_accessoars = price_from_ball / 5

sum = price_from_one_year +price_from_shoes + price_from_uniform + price_from_ball + price_from_accessoars

print(sum)