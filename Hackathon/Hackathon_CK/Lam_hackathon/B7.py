def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

def main():
    numbers = [5, 1, 8, 92, -1, 30]
    print("Original list:")
    print(*numbers)

    bubble_sort(numbers)

    print("Sorted list:")
    print(*numbers)

if __name__ == "__main__":
    main()
