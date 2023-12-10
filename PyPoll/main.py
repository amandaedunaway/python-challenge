#import necessary libraries

# read the csv file: input with file path 
# seperate the data with comma delimiter
# need to be able to read and write to the file?


#print("Election Results")
#print("-------------------------")

# for loop to utilize all rows
    #for i from 2 to length of data

        # Total number of votes in the dataset:
            #calculation: sum the number of i's (starting from line 2) 
            # or we could just say the total votes is the length of data - 1 (no loop needed)
            # we can define the length of the data as a variable to refer to each time
                #print("Total Votes:": total votes calc)

    #print("-------------------------")

        # Complete list of candidates who received votes:
            #calculation: Candidates() = use the "unique" function to find the unique names
            #creates a list or dictionary of candidates

        # The percentage and total votes each candidate won:
            # is there a count function? could search column 3 and use "count" for each name
            # or search all rows and count the number of times each name appears: 
                # ccc = 0
                # if row i, column 3 = "Charles Casper Stockham" then ccc = ccc + 1 else nothing.
                # calculation: (ccc/total votes calc)*100
                #print("Candidates(0):": total votes calc (ccc))
            # do the same for other 2 candidates 

    #print("-------------------------")

# The winner of the election based on popular vote
    #calculation: find the max value of Candidates()
    #print("Winner:", max value candidates calculation)

 #print("-------------------------")


#Addtional requirements:
#Analysis prints to terminal as code runs
#Export text file with the results:
    #unsure how to do this part