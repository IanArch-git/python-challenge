
total_months = 0
total_pl = 0.00
chgProfits = 0
profit = 0
avgAvg = 0

profitList = []
moChanges = []
date = []


import csv
file_path = "budget_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    Date = csv_header.index('Date')
    PL = csv_header.index('Profit/Losses')

    for row in csvreader:
        #Count months
        total_months = total_months + 1
        
        #Calc total PL
        total_pl = total_pl + int(row[PL])

        #Calc Monthly Change, store in list, reset for next row
        moNum = float(row[1])
        change = moNum - profit
        moChanges.append(change)
        chgProfits = chgProfits + change
        profit = moNum

    #print(moChanges)

        #Calc avg change
        avgAvg = chgProfits/total_months

    #Add dates to new date list
        date.append(row[0])

    print(avgAvg)


    
   

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_pl}")
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