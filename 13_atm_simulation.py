# Case Study 13: ATM Transaction Sequence Simulation

print("ATM TRANSACTION SIMULATION")
balance = 5000
transactions = [
    ("Deposit", 2000),
    ("Withdrawal", 1500),
    ("Withdrawal", 4000),
    ("Deposit", 500),
    ("Withdrawal", 1000)
]

successful = 0
rejected = 0

for transaction in transactions:
    transaction_type, amount = transaction

    if amount <= 0:
        print("Rejected: Invalid amount", amount)
        rejected += 1
    elif transaction_type == "Deposit":
        balance += amount
        successful += 1
        print("Deposit successful:", amount)
    elif transaction_type == "Withdrawal":
        if amount > 3000 or amount > balance:
            print("Withdrawal rejected:", amount)
            rejected += 1
        else:
            balance -= amount
            successful += 1
            print("Withdrawal successful:", amount)
    else:
        print("Rejected: Unknown transaction")
        rejected += 1

print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)
print("Final Balance: Rs.", balance)
