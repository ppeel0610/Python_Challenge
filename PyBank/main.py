#import budget data 
import os
import csv 

#working directory
budget_csv = os.path.join('Resources','budget_data.csv')

#Make lists 
Total_month = 0
Total_net = 0 
Average = []
Greatest_Increase = []
Greatest_Decrease = []
monthly_changes = 0 
#read in CSV
with open(budget_csv) as csvfile : 
    budget_data = csv.reader(csvfile, delimiter = ",")
    # print(csv_reader)
    

    #Skip the header Row and the first month
    header = next(budget_data) 
    first_month = next(budget_data)
    print(first_month)

    #Set the total month & totalnet variables to include first month data 
    Total_month = Total_month + 1 
    Total_net = Total_net + int(first_month[1])
    previous_net= int(first_month[1])
    # print(Total_net)
    # print(previous_net)

    print("Financial Analysis")
    print("---------------------")

    #For  Loop to Run the csv file to get table information
    for row in budget_data: 
        Total_month = Total_month + 1
    

# The net total amount of "Profit/Losses" over the entire period
        Total_net=Total_net+ int(row[1])
    
    print(f'Total Months: {Total_month}')
    print(f'Total: ${Total_net}')    

#Average  Change: $-2315.12 The average of the changes in "Profit/Losses" over the entire period


#make List to reference in average 
# Total_month.append(row[1])
# Total_net.append(int(row[1]))

#     for row in len(Total_net)-1):
#     monthly_changes.append(Total_net[x+1]- Total_net[x])
# print(f"Average Change: {round(sum(monthly_changes)/len(Total_month),2)}")

# max_increase_value = max(monthly_changes)
# max_decrease_value = min(monthly_changes)
