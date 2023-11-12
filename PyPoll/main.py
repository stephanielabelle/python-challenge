# importing required modules
import csv
import os

# defining path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

# variable for tracking total number of votes
ballot_count = 0 

# list that identifies individual candidate names
candidate = []

# list that pulls all names of votes in dataset
total_can_list = []

# using csv reader to read the csv file following the previously defined "csvpath"
with open(csvpath,"r") as pollcsv:
    csvreader = csv.reader(pollcsv, delimiter=',')
    
    # removes header of csv file
    poll_header = next(pollcsv)

    # moves through csv row by row
    for row in csvreader: 

        # populating list of all votes by name
        total_can_list.append(row[2])
        
        # putting only unique candidate names in a list called "candidate"
        if row[2] not in candidate:
            candidate.append(row[2])
        
        # counts number of ballots 
        ballot_count += 1

# list that holds the total number of votes by candidate
tally = []

# variable to tally votes for candidates
tallyentry = 0

# length of candidate list to determine how many candidates and utilize for list range
length = len(candidate)

# moving through candidate list to calculate total number of votes received
for x in range(0,length):
    
    #defining candidate name
    name = candidate[x]
    
    # moving through total_can_list to count how many votes per candidate
    for entry in total_can_list:
        if entry == name:
            tallyentry +=1

    # addition of total number of votes per candidate to vote "tally" list
    tally.append(tallyentry)
    
    # resetting number of votes before moving onto next candidate
    tallyentry=0

# finding maximum number of votes per candidate in tally list
# finding index of vote number in tally list
# finding corresponding name in candidate list with index
winner = max(tally)
win_index = tally.index(winner)
win_name = candidate[win_index]

# Defining lines for output
line1 = f'Election Results'
line2 = f'-------------------------'
line3 = f'Total Votes: {ballot_count}'
line4 = f'Winner: {win_name}'

# making output into a list
block1 = [line1,line2,line3,line2]
block2 = [line2,line4,line2]

# Printing to Terminal
for j in block1:
    print(j)
for x in range(0,length):
    print(f'{candidate[x]}: {round((tally[x]/ballot_count*100),3)}% ({tally[x]})')
for k in block2:
    print(k)

# Writing to text file stored in analysis folder
# defining path
resultpath = os.path.join("PyPoll", "analysis", "election_analysis.txt")

# writing in election_analysis text file 
# utlize '\n' for line breaks
with open(resultpath,'w')as t:
    for j in block1:
        t.write(j)
        t.write('\n')
    for x in range(0,length):
        t.write(f'{candidate[x]}: {round((tally[x]/ballot_count*100),3)}% ({tally[x]})')
        t.write('\n')
    for k in block2:
        t.write(k)
        t.write('\n')
