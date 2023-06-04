import random

numbers = random.sample(range(1, 100), 5)
print("Danh sách các số:", numbers)

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print("các số chẵn trong danh sách:", even_numbers)
