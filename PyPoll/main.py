# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

total_votes = 0
candVotes = []
candPercent = []


import csv
file_path = "election_data.csv"

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    VoterID = csv_header.index('Voter ID')
    County = csv_header.index('County')
    Candidate = csv_header.index('Candidate')
    candz = []

    for row in csvreader:
        #Count votes
        total_votes = total_votes + 1
        
        #Count candidates and add to list
        candz.append(str(row[Candidate]))

    #Return only unique values from candz list
    unique_candz = list(set(candz))

    #Count candidates from candz list
    cand1 = unique_candz[0]
    cand1_count = candz.count(cand1)

    cand2 = unique_candz[1]
    cand2_count = candz.count(cand2)

    cand3 = unique_candz[2]
    cand3_count = candz.count(cand3)

    cand4 = unique_candz[3]
    cand4_count = candz.count(cand4)

    cand1_percent = round((cand1_count / total_votes)*100)
    cand2_percent = round((cand2_count / total_votes)*100)
    cand3_percent = round((cand3_count / total_votes)*100)
    cand4_percent = round((cand4_count / total_votes)*100)

    maxList = [cand1_percent, cand2_percent, cand3_percent, cand4_percent]
    

    #print(unique_candz)

    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"{cand1}: {cand1_percent}.000% ({cand1_count})")
    print(f"{cand2}: {cand2_percent}.000% ({cand2_count})")
    print(f"{cand3}: {cand3_percent}.000% ({cand3_count})")
    print(f"{cand4}: {cand4_percent}.000% ({cand4_count})")
    print("-------------------------")
    #print(Winner)
    #print("-------------------------")

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