# Предпазен найлон - 1.50 лв. за кв. метър
# Боя - 14.50 лв. за литър
# Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира
# се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички
# разходи за материали.


required_amount_of_naylon = int(input())
necessary_amount_of_paint = int(input())
amount_of_diluent = int(input())
work_hour = int(input())

price_from_naylon = (required_amount_of_naylon + 2) * 1.50
price_from_paint = (necessary_amount_of_paint + (necessary_amount_of_paint * 0.10)) * 14.50
price_from_diluent = amount_of_diluent * 5
all_sum = price_from_naylon + price_from_paint + price_from_diluent + 0.40

workers_sum = (all_sum * 0.30) * work_hour
finish_sum = all_sum + workers_sum

print(finish_sum)