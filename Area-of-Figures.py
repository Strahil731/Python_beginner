import math

figures_type = input()
area = 0

if figures_type == 'square':
    side_A = float(input())
    area = side_A * side_A
elif figures_type == 'rectangle':
    side_A = float(input())
    side_B = float(input())
    area = side_A * side_B
elif figures_type == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
elif figures_type == 'triangle':
    side_A = float(input())
    height = float(input())
    area = side_A * height / 2

print(f"{area:.3f}")