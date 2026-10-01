# Strategy Classes
class CreditCard:
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using Credit Card.")


class DebitCard:
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using Debit Card.")


class UPI:
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using UPI.")


class NetBanking:
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using Net Banking.")


# Context Class
class Payment:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)


print("Select Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")

choice = int(input("Enter Choice: "))
amount = float(input("Enter Amount: "))

if choice == 1:
    payment = Payment(CreditCard())
elif choice == 2:
    payment = Payment(DebitCard())
elif choice == 3:
    payment = Payment(UPI())
elif choice == 4:
    payment = Payment(NetBanking())
else:
    print("Invalid Choice")
    exit()

payment.process(amount)

"""
Select Payment Method
1. Credit Card
2. Debit Card
3. UPI
4. Net Banking
Enter Choice: 3
Enter Amount: 25000
Payment of ₹25000.0 done using UPI.
"""
