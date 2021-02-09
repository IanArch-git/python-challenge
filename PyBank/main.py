# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset
total_months = 0

# #   * The net total amount of "Profit/Losses" over the entire period
total_pl = 0.00

# #   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
avg_pl = 0.00

# #   * The greatest increase in profits (date and amount) over the entire period
greatest_incr = {}

# #   * The greatest decrease in losses (date and amount) over the entire period
greatest_decr = {}

import csv
file_path = "budget_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_months = total_months + 1
        #print(row)


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    # print(f"Total: {total_pl}")
    # print(f"Average Change: {avg_change}")
    # print(f"Greatest Increase in Profits: {greatest_incr}")
    # print(f"Greatest Decrease in Losses: {greatest_decr}")
    # print("----------------------------")




# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.