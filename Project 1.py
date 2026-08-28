# Banking Program in python

balance = 5000

print("1. Check Balance")
print("2. Add Money")
print("3. Take Money")

choice = input("Choose an option: ")

if choice == "1":
    print("Your balance is =", balance)

elif choice == "2":
    money = int(input("Enter amount to add: "))
    balance += money
    print("Updated balance =", balance)

elif choice == "3":
    money = int(input("Enter amount to withdraw: "))

    if money <= balance:
        balance -= money
        print("Updated balance =", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid option")