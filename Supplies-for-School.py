# Пакет химикали - 5.80 лв.
# Пакет маркери - 7.20 лв.
# Препарат - 1.20 лв (за литър)


pen_packets = int(input())
marker_packets = int(input())
detergent_liters = int(input())
reduction_percent = int(input())

sum_from_pen =  pen_packets * 5.80
sum_from_marker = marker_packets * 7.20
sum_from_reduction = detergent_liters * 1.20
all_sum = sum_from_pen + sum_from_marker + sum_from_reduction

need_sum =  all_sum - (all_sum * reduction_percent / 100)

print(need_sum)