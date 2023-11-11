import csv
import os

ballot_count = 0 
# defining path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
print(csvpath)

candidate = []
print(candidate)

with open(csvpath,"r") as pollcsv:
    csvreader = csv.reader(pollcsv, delimiter=',')
    poll_header = next(pollcsv)
    
    for row in csvreader: 
        if row[2] not in candidate:
            candidate.append(row[2])  
        #counts number of ballots 
        ballot_count += 1
        
print(candidate)
# unique_name = set(candidate)
# print(unique_name)      

#             print(candidate)
#         else:
#             for i in candidate:
#                 if(i!=(row[2])):                    
#                     candidate.append(row[2])
# # print(f'here are the candidates {candidate}')
# print(ballot_count)  
# print(candidate)        
