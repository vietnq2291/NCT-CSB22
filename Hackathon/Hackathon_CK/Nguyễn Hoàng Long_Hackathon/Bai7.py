def sort_list(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers = [5, 1, 8, 92, -1, 30]
numbers.sort()
print("Các số trong list sau khi được sắp xếp từ bé đến lớn:", numbers)
