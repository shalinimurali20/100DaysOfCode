#002 Tip Calculator

#greeeting
print("Welcome to Tip Calculator")

#get bill, tip percent and number of poeple
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
split = int(input("How many people to split the bill?"))

#calculate
tip = (1 + tip_percent/100) * total_bill # ((tip_percent/100) * total_bill) + total_bill

#round to 2 decimal places and calculate the pay per person
pay = round(tip/split,2)

#f string
print(f"Each person should pay {pay}") 

# to print exactly with two precision, you can use format function

#  pay = "{:.2f}".format(tip/split)