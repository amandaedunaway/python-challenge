import csv

file_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyBank\Resources\budget_data.csv'
output_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyBank\Analysis\budget_analysis.txt'

total_months = 0
total_net = 0
#month_of_change = []
net_change_list = []
greatest_inc = [0,""]
greatest_dec = [999999999,""]
# print("Financial Analysis")
# print("----------------------------")


##Find Total number of months:
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    first_line = next(csv_reader)
    total_months += 1
    total_net += int(first_line[1])
    previous = int(first_line[1])
    for row in csv_reader:
        total_months +=1
        total_net += int(row[1])
        net_change = int(row[1]) - previous
        net_change_list.append(net_change)
        previous = int(row[1])
        #month_of_change.append(row[0])

        if net_change > greatest_inc[0]:
            greatest_inc[0] = net_change
            greatest_inc[1] = row[0]

        if net_change < greatest_dec[0]:
            greatest_dec[0] = net_change
            greatest_dec[1] = row[0]

         # Total number of months in the dataset = number of rows
        #row_count = sum(1 for row in csv_reader) + 1
#print("Total Months: "+str(row_count))
monthly_average_change = sum(net_change_list)/len(net_change_list)
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
# ##Find Net total amount of Profit/Losses:
# column_to_sum = 'Profit/Losses'
# column_sum = 0

with open(output_path, 'w') as txt_file:
    txt_file.write(results)




