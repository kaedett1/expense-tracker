# Project: Expense Tracker
# Installment 2: Talking to the User
# Author: Allen Brent S. Mañago
# Description: Asks for a name and two expenses, then shows a summary.

print("=" * 40)
print("\tEXPENSE TRACKER\n\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t\t${total}")
print(f"Average:\t\t${average}")
print("-" * 40)
print("Made by: Allen Brent S. Mañago  |  Installment 2")