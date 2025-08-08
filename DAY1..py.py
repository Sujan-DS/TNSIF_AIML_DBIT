#!/usr/bin/env python
# coding: utf-8

# In[ ]:


correct_pin = "1234"
balance = 10000
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. Welcome!")

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your balance is Rs", balance)

            elif choice == "2":
                amount = float(input("Enter amount to deposit: Rs "))
                if amount > 0:
                    balance += amount
                    print("Rs", amount, "deposited successfully.")
                else:
                    print("Invalid amount.")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: Rs "))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    print("Rs", amount, "withdrawn successfully.")
                else:
                    print("Insufficient balance or invalid amount.")

            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        break
    else:
        attempts -= 1
        print("Incorrect PIN. Attempts left:", attempts)
        if attempts == 0:
            print("Too many wrong attempts. Card blocked.")

