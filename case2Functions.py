from cs50 import SQL
from sys import argv

# Open database for writing
open(f"customerOrders.db", "r")
db = SQL("sqlite:///customerOrders.db")

def revForYear(y):
    totalRevenue = db.execute("SELECT SUM(net_revenue) FROM customerOrders WHERE year = :year", year=y)
    rev = totalRevenue[0].get('SUM(net_revenue)')
    return rev
    
    
def newCustomerRev(y):
    
    newPeople = db.execute("SELECT customer_email, net_revenue FROM customerOrders WHERE customer_email NOT IN (SELECT customer_email FROM customerOrders WHERE year = :year )", year=(y-1))
    return newPeople
    
def customerGrowth(y):
    curr = db.execute("SELECT SUM(net_revenue) FROM customerOrders WHERE year = :year", year=y)
    prev = db.execute("SELECT SUM(net_revenue) FROM customerOrders WHERe year = :year", year= (y - 1))
    
    growth = curr[0].get('SUM(net_revenue)') - prev[0].get('SUM(net_revenue)')
    
    return growth
    


# calculate revenue based on customers that left from the previous year and what the revenue was that year

def customerAttrition(y):
    
    lastYear = db.execute("SELECT SUM(net_revenue) FROM customerOrders WHERE customer_email NOT IN (SELECT customer_email FROM customerOrders WHERE year = 2016)")

    customersLeave = db.execute("SELECT SUM(net_revenue) FROM customerOrders WHERE customer_email NOT IN (SELECT customer_email from customerOrders WHERE year = :year1)  AND year = :year2", year1 = y, year2 = (y - 1))
    return customersLeave
    

def customerRevCurr(email, y):
    customerRevenue = db.execute("SELECT net_revenue FROM customerOrders WHERE customer_email = :customer_email AND year = :year", customer_email=email, year=y)
    return customerRevenue


def customerRevPrior(email, y):
    customerRevenue = db.execute("SELECT net_revenue FROM customerOrders WHERE customer_email = :customer_email AND year = :year", customer_email=email, year=(y-1))
    return customerRevenue


def customerCountCurr(y):
    customerCount = db.execute("SELECT COUNT(DISTINCT customer_email) FROM customerOrders WHERE year = :year", year=y)
    return customerCount
    
    
def customerCountPrev(y):
    customerCount = db.execute("SELECT COUNT(DISTINCT customer_email) FROM customerOrders WHERE year = :year", year=(y-1))
    return customerCount
    

def newCustomers(y):
    newPeople = db.execute("SELECT customer_email FROM customerOrders WHERE customer_email NOT IN (SELECT customer_email FROM customerOrders WHERE year = :prev) AND year = :curr", prev = (y-1), curr=(y))
    return newPeople
    
    
def lostCustomers(y):
    lostPeople = db.execute("SELECT TRIM(customer_email) FROM customerOrders WHERE customer_email NOT IN (SELECT TRIM(customer_email) FROM customerOrders WHERE year = :curr) AND year = :prev", prev=(y-1), curr=y)
    return lostPeople
    

print("Total Revenue (2015): ")
print(revForYear(2016))
print()

print("New Customer Revenue (2016): ")
print(newCustomerRev(2016))
print()

print("Existing Customer Growth (2016): ")
print(customerGrowth(2016))
print()

print("Attrition Loss (2017): ")
print(customerAttrition(2017))
print()

print("Customer (mobvusnzfr@gmail.com) Revenue Current Year (2015): ")
print(customerRevCurr('mobvusnzfr@gmail.com', 2015))
print()

print("Customer (mwrossuukz@gmail.com) Revenue Prior Year (2015)")
print(customerRevPrior('mwrossuukz@gmail.com', 2016))
print()

print("Total Customers in 2016: ")
print(customerCountCurr(2016))
print()

print("Total Customers last year (2015): ")
print(customerCountPrev(2016))
print()

print("New Customers in 2017: ")
print(newCustomers(2017))
print()

print("Lost Customers in 2017: ")
print(lostCustomers(2017))
print()