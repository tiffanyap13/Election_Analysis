#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

#Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # To do: peform analysis.
#     print(election_data)

import csv
import os

 # Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
 # Open the election results and the read file.
# with open(file_to_load) as election_data:
#     #Print the file object.
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# #Using the open() function with the "w" mode we will write data to the file
# open(file_to_save, "w")

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# # Close the file.
# outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Candidate Votes, declare empty dictionary
candidate_votes = {}
# Winning candidate & winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the electoin results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze data here.
    file_reader = csv.reader(election_data)
    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        # Read in the candidate name for this ballot
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    #Save to text file   
    with open(file_to_save, "w") as txt_file:
            # Determine winning vote count and candidate
            # Determine if votes greater than winning count
    # Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------------\n")
        print(election_results, end="")
            # Save final vote count to the text file.
        txt_file.write(election_results)
                
   
        #Determine % votes
        #1. Iterate through list.
        for candidate_name in candidate_votes:
            #2. Retrieve vote count
            votes = candidate_votes[candidate_name]
            #3. calc % of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #To do: print candidates name, vote count, percentage of votes to terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2 If true, set winning_count = votes and winning_percent = #vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #3. set winning_candidate equal to candidate's name.
                winning_candidate = candidate_name
            #4. print name and %
            # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            #print the candidate name from each row

            # # Add the candidate name to the candidate list.
            # candidate_options.append(candidate_name)
                winning_candidate_summary = (
                    f"---------------------------\n"
                    f"Winner: {winning_candidate}\n"
                    f"Winning Vote Count: {winning_count:,}\n"
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                    f"---------------------------\n")
                #print(winning_candidate_summary)
                # print each candidate, count & % to terminal.
            print(candidate_results)
            # Save candidate result to text file.
            print(winning_candidate_summary)
            txt_file.write(candidate_results)
        # Save the winning candidate's name to text file.
        txt_file.write(winning_candidate_summary)


    # Print the total number of ballots
    # print(total_votes)

    # # Print the candidate list.
    # print(candidate_options)

    # Print the candidate vote dictionary.
    # print(candidate_votes)


    


