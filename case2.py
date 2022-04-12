import csv
from sys import argv
from cs50 import SQL



#Feature Set
def total_credit_limit(months_since_inquiry):
    return credit_limit

def avg_interest_rate(state):
    return interest

def annual_income(job_title):
    return income

def avg_loan(ownership_type):
    return amount

def avg_loan_amount(purpose):
    return amount



db = SQL("sqlite:///customerOrders.db")

if len(argv) != 2:
    print("ERROR")
    exit(1)

with open(argv[1], 'r') as customer_orders:

    # Use DictReader
    reader = csv.DictReader(customer_orders, delimiter=",")

    # csv file not fully loaded - too large
    for row in reader:
        db.execute("INSERT INTO customerOrders (num, customer_email, net_revenue, year) VALUES (?, ?, ?, ?)", row[""], row["customer_email"], row["net_revenue"], row["year"])


