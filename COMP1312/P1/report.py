company_name = input("Company Name: ")
weekly_revenue = []
weekly_expenses = []


for day in range(7):
    daily_revenue = int(input(f"Daily Revenue {day + 1 }: "))
    daily_expenses = int(input(f"Daily Expenses for day {day + 1}: "))
    weekly_revenue.append(daily_revenue)
    weekly_expenses.append(daily_expenses)

weekly_profit = sum(weekly_revenue) - sum(weekly_expenses)
weekly_profit_margin = weekly_profit / sum(weekly_revenue)

lucrative = False
if weekly_profit_margin >= 0.75:
    lucrative = True
    print(f"{company_name} was lucrative this week")

if sum(weekly_revenue) > sum(weekly_expenses):
    made_profit = True
    if lucrative == False:
        print(f"{company_name} made a profit this week")
else:
    made_profit = False
    print(f"{company_name} did not make a profit this week")

print(f"Weekly Revenue: £{sum(weekly_revenue)}")
print(f"Weekly Expenses: £{sum(weekly_expenses)}")
print(f"Weekly Profit: £{weekly_profit}")
print(f"Weekly Profit Margin: {weekly_profit_margin}")
#print(f"Most Profitable Day: {weekly_revenue.index(max(weekly_revenue)) + 1}")
#print(f"Most Expensive Day: {weekly_expenses.index(max(weekly_expenses)) + 1}")
