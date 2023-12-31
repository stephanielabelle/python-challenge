# importing csv and os modules
import csv
import os

# variable to determine number of entries after header
rowcount = 0

# variable to determine net total amount of Profit/Losses
net_total = 0

# variables to populate profit/loss monthly "difference" list (diff_list) and corresponding "date" list (date_diff_list)
# variables/lists used for calculation of average Profit/Losses, greatest increase/decrease in profits
num_1 = 0
num_2 = 0
diff_list = []
date_diff_list = []

# defining path to csv file
budgetpath = os.path.join('Pybank','Resources', 'budget_data.csv')

# opening and reading csv file with csv module
with open(budgetpath,"r",) as budget_csv:
    csvreader = csv.reader(budget_csv)
    
    # Removing header from csv analysis 
    budget_header = next(budget_csv)
    
    # reading row by row in csv document
    for row in csvreader:

        # to count how many months of data
        rowcount += 1

        # finding the total amount of profit/losses in the whole dataset
        net_total +=int(row[1])
        
        # setting variables and calculate profit/loss changes (num_1 and num_2)
        # num_1 and num_2 are defined based on if the rowcount is even or odd
        # populating list with profit/loss changes (diff_list) and corresponding date (date_diff_list)
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

# calculting average change of profit/lossses over the entire period
avg_change = sum(diff_list)/(rowcount-1)  

# finding the greatest increase/decrease in profit/loss change and finding the index to determine corresponding date
greatest_incr = max(diff_list)    
greatest_decr = min(diff_list)
max_index = diff_list.index(greatest_incr)
min_index = diff_list.index(greatest_decr)
max_date = date_diff_list[max_index]
min_date = date_diff_list[min_index]

# final data to terminal and text file
line1 = 'Statstical Analysis'
line2 = '---------------------------------'
line3 = f'Total Months: {rowcount}'
line4 = f'Total: ${net_total}'
line5 = f'Average Change: ${round(avg_change,2)}'
line6 = f'Greatest Increase in Profits: {max_date} (${greatest_incr})'
line7 = f'Greatest Decrease in Profits: {min_date} (${greatest_decr})'

# make summary statistics into a list for easier printout
stat_list = [line1,line2,line3,line4,line5,line6,line7]

# final data printed to terminal and written to text file
output_path = os.path.join("PyBank", "analysis", "final_analysis.txt")
with open(output_path,'w') as t:
    for x in stat_list:
        t.write(x)
        t.write("\n")
        print(x)






     


