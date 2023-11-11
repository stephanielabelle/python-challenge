import csv
import os
rowcount = 0
net_total = 0
num_1 = 0
num_2 = 0
diff_list = []
date_diff_list = []

# defining path to csv file
budgetpath = os.path.join('..','Resources', 'budget_data.csv')

with open(budgetpath,"r",) as budget_csv:
    csvreader = csv.reader(budget_csv)
    budget_header = next(budget_csv)
    for row in csvreader:
        rowcount += 1
        net_total +=int(row[1])
        if rowcount == 1:
            num_1 = int(row[1])
        elif (rowcount % 2) == 0:
            num_2 = int(row[1])
            difference = (num_2 - num_1)
            diff_list.append(difference)
            date_diff_list.append(row[0])
        elif ((rowcount % 2) !=0) and (rowcount > 1):
            num_1 = int(row[1])
            difference = (num_1 - num_2)
            diff_list.append(difference)
            date_diff_list.append(row[0])

avg_change = sum(diff_list)/(rowcount-1)  
greatest_incr = max(diff_list)    
greatest_decr = min(diff_list)
max_index = diff_list.index(greatest_incr)
min_index = diff_list.index(greatest_decr)
max_date = date_diff_list[max_index]
min_date = date_diff_list[min_index]

print("")
print("Statistical Analysis")
print("---------------------------------")
print(f'Total Months: {rowcount}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(avg_change,2)}')
print(f'Greatest Increase in Profits: {max_date} (${greatest_incr})')
print(f'Greatest Decrease in Profits: {min_date} (${greatest_decr})')




     


