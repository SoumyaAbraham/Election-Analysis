#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load= os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save= os.path.join("analysis", "election_analysis.txt")


#Initialize total votes counter
total_votes=0
candidate_options=[]
candidate_votes={}

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To Do: read and analyze data here
    file_reader=csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)

    #print each row in the csv file

    for row in file_reader:
        #2. Add to the total votes
        #total_votes +=1
        total_votes=total_votes+1

        #print the candidate name from each row
        candidate_name=row[2]

        #Only add name if name does not match existing candidate
        if candidate_name not in candidate_options:

            #Add candidate name to candidate list
            candidate_options.append(candidate_name)

            #Track candidate's vote count
            candidate_votes[candidate_name] = 0

         #Add a vote to the candidate's vote
        candidate_votes[candidate_name]+=1
        #that is the same as candidate_votes[candidate_name]=cnadidate_votes[candidate_name]+1



#Print the candidate vote dictionary
print(candidate_votes, "\n")

#Print candidate list
print(candidate_options, "\n")


#1. Iterate through candidate list
for candidate_name in candidate_votes:
    #2. Retrieve the vote counts per candidate
    votes=candidate_votes[candidate_name]
    #3. Calculate percentage
    vote_percentage=float(votes)/float(total_votes)*100

#4. print candidate name and percentage
    print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote\n")
