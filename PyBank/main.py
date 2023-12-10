# Import library and establish file paths to read and write
import csv

file_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyBank\Resources\budget_data.csv'
output_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyBank\Analysis\budget_analysis.txt'


# Initialize variables and lists
total_months = 0                # total months in the dataset
total_net = 0                   # net total amount of "Profit/Losses"
net_change_list = []            # empty list to fill in with month-to-month changes
greatest_inc = [0,""]           # list to fill in greatest increase in profits and corresponding date
greatest_dec = [999999999,""]   # list to fill in greatest decrease in profits and corresponding date


# Open the file and find results
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)       # read the file
    header = next(csv_reader)               # designate header row as first row of file
    first_line = next(csv_reader)           # designate the first row of data as second row of file
    total_months += 1                       # add 1 to the count of months
    total_net += int(first_line[1])         # add the profit for the row to the cumulative total 
    previous = int(first_line[1])           # designate the profit as the "previous" value for future comparison

    for row in csv_reader:                  # For each remaining row in the data, do the following:
        total_months +=1                        # add 1 to the count of months
        total_net += int(row[1])                # add the profit for the row to the cumulative total
        net_change = int(row[1]) - previous     # subtract last month's profit from this month's profit
        net_change_list.append(net_change)      # add this month's change in profit to the net change list
        previous = int(row[1])                  # designate this month's profit as the "previous" value for next row

        if net_change > greatest_inc[0]:        # If this month's change in profit exceeds the greatest increase in profit so far,
            greatest_inc[0] = net_change        # record this month's change in profit as the greatest increase
            greatest_inc[1] = row[0]            # and record this date 

        if net_change < greatest_dec[0]:        # If this month's change in profit is lower than the greatest decrease in profit so far,
            greatest_dec[0] = net_change        # record this month's change in profit as the greatest decrease
            greatest_dec[1] = row[0]            # and record this date

# Calculate the average change of the dataset by summing all the monthly changes and dividing by the number of data points in the list
monthly_average_change = sum(net_change_list)/len(net_change_list)


# Set up the text outline for the analysis results and input the values found above
# Display the results in the terminal
results = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${monthly_average_change:.2f}
Greatest Increase in Profits: {greatest_inc[1]} (${greatest_inc[0]})
Greatest Decrease in Profits: {greatest_dec[1]} (${greatest_dec[0]})
"""
print(results)


# Write the results to a txt file, located in the specified output path
with open(output_path, 'w') as txt_file:
    txt_file.write(results)




