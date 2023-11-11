import csv
import os

ballot_count = 0 
# defining path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
print(csvpath)

with open(csvpath,"r") as pollcsv:
    csvreader = csv.reader(pollcsv)
    poll_header = next(pollcsv)
    
    for row in csvreader:   
        #counts number of ballots 
        ballot_count += 1