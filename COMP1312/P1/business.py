company_name = input("Company Name: ")
daily_revenue = int(input("Daily Revenue: "))
daily_expenses = int(input("Daily Expenses: "))

daily_profit = daily_revenue - daily_expenses
daily_profit_margin = daily_profit / daily_revenue

lucrative = False
if daily_profit_margin >= 0.75:
    lucrative = True
    print(f"{company_name} was lucrative today")

if daily_revenue > daily_expenses:
    made_profit = True
    if lucrative == False:
        print(f"{company_name} made a profit today")
else:
    made_profit = False
    print(f"{company_name} did not make a profit today")

print(f"Daily Revenue: £{daily_revenue}")
print(f"Daily Expenses: £{daily_expenses}")
print(f"Daily Profit: £{daily_profit}")
print(f"Daily Profit Margin: £{daily_profit_margin}")
