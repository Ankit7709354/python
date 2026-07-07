inventory = {}

while True:

    product = input("Product (exit to stop): ")

    if product.lower() == "exit":
        break

    quantity = int(input("Quantity: "))

    inventory[product] = quantity

print("\nInventory")

for product, quantity in inventory.items():
    print(product, "-", quantity)