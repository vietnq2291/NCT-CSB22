def fibonacci_sequence(n):
    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

def main():
    while True:
        try:
            n = int(input("Input a number (> 0): "))
            if n <= 0:
                print("Please input a number bigger than 0 (> 0).")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    fib_numbers = fibonacci_sequence(n)
    print(f" First {n} Fibonacci numbers: ")
    for num in fib_numbers:
        print(num, end=" ")

if __name__ == "__main__":
    main()