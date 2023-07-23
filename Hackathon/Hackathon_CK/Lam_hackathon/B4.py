def order_food():
    ordered_items = []

    while True:
        item = input("Please choose a dish: ")

        if item in ordered_items:
            print("You chose this already.")
        else:
            ordered_items.append(item)
            print("Great choice!")

        choice = input("Anything else? (y/n): ")
        if choice.lower() != "y":
            break

    print("\nWell done! Your order:")
    for i in ordered_items:
        print("- " + i)

print("== Welcome to MindX Restaurant ==")

order_food()