length = int(input())
width = int(input())
height = int(input())
percent = float(input())

all_tank_liters = length * width * height
all_liters = all_tank_liters / 1000
need_water = all_liters - (all_liters * percent / 100)

print(need_water)