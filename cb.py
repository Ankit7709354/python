contacts = []

while True:

    name = input("Enter Name (exit to stop): ")

    if name.lower() == "exit":
        break

    phone = input("Phone: ")

    contacts.append([name, phone])

print("\nContacts")

for contact in contacts:
    print(contact[0], "-", contact[1])