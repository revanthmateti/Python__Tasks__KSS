
# Small Shop Customer Purchase Management System

# 1. Dictionary - Store product names and prices
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

# 2. Set - Store product categories
categories = {"Stationery"}

# 3. Tuple - Store product details
product_details = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Stationery"),
    ("Pencil", 5, "Stationery")
)

# 4. List - Store cart items
cart = []


# 5. Recursive function to calculate total price
def total_price(items):

    # Base condition
    if len(items) == 0:
        return 0

    # Calculate current item's price
    item_total = items[0][1] * items[0][2]

    # Recursive call
    return item_total + total_price(items[1:])


# 6. Function to display products
def display_products():

    print("\nAvailable Products:")

    for name, price in products.items():
        print(name, ":", price)


# 7. Function to add items to cart
def add_to_cart():

    try:
        name = input("Enter product name: ")

        # Check whether product exists
        if name not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        price = products[name]

        # Store product name, quantity and price as a tuple
        cart.append((name, quantity, price))

        print("Item added to cart successfully.")

    except ValueError:
        print("Invalid quantity! Please enter a number.")

    except NameError:
        print("Product not found in store.")


# 8. Function to calculate and display total bill
def calculate_bill():

    try:
        if len(cart) == 0:
            print("Your cart is empty.")
            return

        print("\nItems in Cart:")

        # Display cart items
        for item in cart:

            if (not isinstance(item, tuple)
                or len(item) != 3
                or not isinstance(item[0], str)
                or not isinstance(item[1], int)
                or not isinstance(item[2], (int, float))):
                raise TypeError

            print(item[0], "x", item[1])

        # Calculate total using recursion
        total = total_price(cart)

        print("Total Bill:", total)

    except TypeError:
        print("Cart data type error.")

    except ZeroDivisionError:
        print("Calculation error: division by zero.")


# 9. Main menu using while loop
while True:

    print("\n1. Display Products")
    print("2. Add Item to Cart")
    print("3. View Total Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            display_products()

        elif choice == 2:
            add_to_cart()

        elif choice == 3:
            calculate_bill()

        elif choice == 4:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Please enter a valid menu number.")
