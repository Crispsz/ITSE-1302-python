#!/usr/bin/env python3
#interest_calculator.py

year = int()

while(True):

    investment_amount = int(input("Investment Amount: "))

    if investment_amount < 0 or investment_amount > 50000:
        print("Please enter a value greater than 0 and less than 50,000!")

    else: 
        break
    
while(True):

    interest_rate = int(input("Interest Rate: "))

    if interest_rate < 0 or interest_rate > 15:
        print("Please enter a value greater than 0 and less than 15!")

    else: 
        interest_rate_monthly = float(interest_rate/1200)
        break

while(True):

    investment_duration = int(input("Investment Duration: "))

    if investment_duration < 0:
        print("Please enter a value greater than 0!")

    else: 
        investment_duration_monthly = investment_duration * 12
        break

total_value = float(0)

for i in range(investment_duration_monthly, 0, -1):
    total_value += investment_amount
    total_value += total_value*interest_rate_monthly
    if (i-1) % 12 == 0 and i != investment_duration_monthly:
        year += 1
        print(f'Year {year}: ${round(total_value, 2)}')

print(f'\nInvestment Duration: {investment_duration} years')
print(f'Yearly Interest Rate: {float(interest_rate)}%')
print(f'Monthly Investment Amount: ${investment_amount}')
print(f'Total Amount of Investment After Compounding: ${round(total_value, 2)}')
print("-------------------------------------------------------------------\nWritten by Peyton Tharp")
