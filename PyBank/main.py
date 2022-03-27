'''PyBank Challenge
The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period'''

import os
import csv

PyBank_csv = os.path.join("Resources", "budget_data.csv")

date = []
profit = []
change = []

count = 0
total_profit = 0
total_change = 0
initial_profit = 0

with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        date.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])

        if initial_profit == 0:
            change_profit = 0
        else:
             change_profit = final_profit - initial_profit

        #print(change_profit)

        change.append(change_profit)
        total_change = total_change + change_profit
        initial_profit = final_profit

        #print("Hi", initial_profit)

        count = count + 1

    average_change = total_change / (count - 1)

    #print(change)

    greatest_increase_profits = max(change)
    greatest_decrease_profits = min(change)

    increase_date = date[change.index(greatest_increase_profits)]
    decrease_date = date[change.index(greatest_decrease_profits)]    

    #print(count)
    #print(total_change)

    print("Financial Analysis")
    print("----------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(float(average_change),2)))
    print("Greatest Increase in Profits: " + str(increase_date) 
    + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) 
    + " ($" + str(greatest_decrease_profits)+ ")")
    
#Output_path = os.path.join("..", "analysis", new.csv)
with open("analysis/PyBank.txt", 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------\n") 
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(round(float(average_change),2)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) 
    + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) 
    + " ($" + str(greatest_decrease_profits) + ")\n")
    
