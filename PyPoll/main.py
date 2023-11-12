import csv
import os

ballot_count = 0 
# defining path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')


candidate = []
total_can_list = []
num_votes_c0 = 0
num_votes_c1 = 0
num_votes_c2 = 0


with open(csvpath,"r") as pollcsv:
    csvreader = csv.reader(pollcsv, delimiter=',')
    poll_header = next(pollcsv)

    
    for row in csvreader: 
        total_can_list.append(row[2])
        if row[2] not in candidate:
            candidate.append(row[2])
        
        #counts number of ballots 
        ballot_count += 1

tally = []
tallyentry = 0
length = len(candidate)
for x in range(0,length):
    name = candidate[x]
    for entry in total_can_list:
        if entry == name:
            tallyentry +=1
    tally.append(tallyentry)
    tallyentry=0

winner = max(tally)
win_index = tally.index(winner)
win_name = candidate[win_index]

# Defining lines for output
line1 = 'Election Results'
line2 = '-------------------------'
line3 = f'Total Votes: {ballot_count}'
line4= f'Winner: {win_name}'

block1 = [line1,line2,line3,line2]
block2 = [line2,line4,line2]
final_number_data = []

# Printing to Terminal
for j in block1:
    print(j)
for x in range(0,length):
    print(f'{candidate[x]}: {round((tally[x]/ballot_count*100),3)}% ({tally[x]})')
for k in block2:
    print(k)

# Writing to text file in Analysis Folder
resultpath = os.path.join("PyPoll", "analysis", "election_analysis.txt")
print(resultpath)

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
