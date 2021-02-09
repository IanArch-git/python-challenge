# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

total_votes = 0
votes_1 = 0
votes_2 = 0
votes_3 = 0 
votes_4 = 0

import csv
file_path = "election_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    VoterID = csv_header.index('Voter ID')
    County = csv_header.index('County')
    Candidate = csv_header.index('Candidate')
    candz = []

    for row in csvreader:
        total_votes = total_votes + 1
        candz.append(str(row[Candidate]))

    #Return only unique values from candz list
    unique_candz = list(set(candz))

    print(unique_candz)


    for row in csvreader:
        if row[Candidate] == unique_candz[0]:
            votes_1 = votes_1 + 1
        

    print(f"{unique_candz[0]} : {votes_1}")


    #print(f"List: {unique_candz}")
    print(f"Total Votes: {total_votes}")
    #print(f"Candidates list: {candz}")
    #print(f"{Candidates[1]} + {votePercentage[1]} + {voteNumbers[1]}") 


#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.