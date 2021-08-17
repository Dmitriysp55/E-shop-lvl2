try:
    quantity = int(input(f'How many?'))
except ValueError:
    quantity = 1

print(quantity)