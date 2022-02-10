class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_pw):
        self.password = new_pw


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, user, amount):
        print("Transfering $" + str(amount), "to", user.name)
        print("Credential required")
        pincode = int(input("Enter your PIN: "))
        if pincode != self.pin:
            print("Invalid Pin")
            return False
        print("Authorized")
        print("Transfering $" + str(amount), "to", user.name)
        self.balance -= amount
        user.balance += amount

        return True

    def request_money(self, user, amount):
        print("You are requesting $" + str(amount), "from", user.name)
        print("Credentials required")

        pin = int(input("Enter " + user.name + "'s PIN: "))
        if pin != user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False

        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction canceled.")
            return False

        print("Request authorized")
        print(user.name + " sent $" + str(amount))

        user.balance -= amount
        self.balance += amount

        return True


"""Driver Code for Task 1"""
# methods are function attached to the class, in that case self.user_name is an attribute
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)


""" Driver Code for Task 2 """
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
user1.change_name("Bobby")
user1.change_pin(5678)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password)


""" Driver Code for Task 3 """
bankuser1 = BankUser("Bob", 1234, "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)


""" Driver Code for Task 4 """
bankuser1 = BankUser("Bob", 1234, "password")
bankuser1.show_balance()
bankuser1.deposit(1000.0)
bankuser1.show_balance()
bankuser1.withdraw(500.0)
bankuser1.show_balance()
amt = 400

""" Driver Code for Task 5"""

bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "newpassword")
bankuser2.deposit(5000.0)
bankuser2.show_balance()
bankuser1.show_balance()
print()

transferred = bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()
print()

if transferred:
    bankuser2.request_money(bankuser1, 300)
    bankuser2.show_balance()
    bankuser1.show_balance()
