# Import library and establish file paths to read and write
import csv

file_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyPoll\Resources\election_data.csv'
output_path = r'C:\Users\aed3h\Documents\Data_Analysis\Module 3 Challenge\python-challenge\PyPoll\Analysis\election_analysis.txt'



# Initialize variables and lists
total_votes = 0                             # total votes in the dataset
candidates_list = []                        # empty list to fill in candidate names
votes_per_cand = [0,0,0]                    # list to fill in the count of each candidate's votes
votes_per_cand_perc = [0,0,0]               # list to calculate the each candidates percentage of total votes



# Open the file and collect the information needed from the file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)       # read the file

    # Set up all initial information needed prior to starting the for loop for the rest of the data
    header = next(csv_reader)               # designate header row as first row of file
    first_line = next(csv_reader)           # designate the first row of data as second row of file
    
    total_votes += 1                        # add 1 to the count of votes for the first row of data

    # add the name in the first row of data to the candidate list
    candidates_list.append(first_line[2])
    # add a vote to the count for the candidate in the corresponding spot in the list   
    votes_per_cand[candidates_list.index(first_line[2])] += 1


    # For each remaining row in the data, do the following:
    for row in csv_reader:                  
        total_votes +=1                     # add 1 to the count of total votes

        # Check if the candidate name in this row matches any of the candidate names recorded in the list.
        # If it is a new name, add it to the candidate list.
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        # add a vote to the count for the candidate in the corresponding spot in the list
        votes_per_cand[candidates_list.index(row[2])] += 1



# Use the information gathered from the file to find the relevant results
# Calculate the percentage of total votes for each candidate, rounded to three decimal places
for candidate in range(len(candidates_list)):
    votes_per_cand_perc[candidate] = round((votes_per_cand[candidate] / total_votes) * 100,3)


# Determine the winner
win_cand_count = max(votes_per_cand)                    # the winning number of votes is the maximum number of votes received by a candidate 
winner_index = votes_per_cand.index(win_cand_count)     # record which spot in the list the winning number was found
winner = candidates_list[winner_index]                  # determine the name of the winner by matching to the corresponding spot in the list


# Set up the text outline for the analysis results and input the values found above
# Display the results in the terminal
results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates_list[0]}: {votes_per_cand_perc[0]}% ({votes_per_cand[0]})
{candidates_list[1]}: {votes_per_cand_perc[1]}% ({votes_per_cand[1]})
{candidates_list[2]}: {votes_per_cand_perc[2]}% ({votes_per_cand[2]})
-------------------------
Winner: {winner}
-------------------------
"""
print(results)



# Write the results to a txt file, located in the specified output path
with open(output_path, 'w') as txt_file:
    txt_file.write(results)
