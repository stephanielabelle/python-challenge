import csv
import os

ballot_count = 0 
# defining path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
print(csvpath)

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
print(length)
for x in range(0,length):
    name = candidate[x]
    print(x)
    print(f'name in x {name}')
    for entry in total_can_list:
        if entry == name:
            tallyentry +=1
    tally.append(tallyentry)
    tallyentry=0
        
line1 = 'Election Results'

        # if row[2] == candidate[0]:
        #     num_votes_c0 += 1
        # elif row[2] == candidate[1]:
        #     num_votes_c1 += 1
        # else:
        #     num_votes_c2 += 1

print(f'{candidate[0]} {num_votes_c0}')
print(f'{candidate[1]} {num_votes_c1}')
print(f'{candidate[2]} {num_votes_c2}')    



        # for person in range(len(candidate)):
        #     if row[2] == candidate(person):
        #         sum(person)=+row[1]
# print(candidate)
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
