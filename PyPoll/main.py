#PyPoll Challenge

#Data: election_data.csv

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

PyPoll_csv = os.path.join("Resources","election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
     
    for row in csvreader:
        count = count + 1
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        unique_candidate.append(x)
        y = candidatelist.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]


print("Election Results")   
print("Total Votes :" + str(count))    
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + (str(format(vote_percent[i], ".3f"))) 
            +"% (" + str(vote_count[i])+ ")")
print("The winner is: " + winner)

with open("analysis/PyPoll.txt", 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + (str(format(vote_percent[i], ".3f"))) 
        +"% (" + str(vote_count[i]) + ")\n")
    text.write("The winner is: " + winner + "\n")





