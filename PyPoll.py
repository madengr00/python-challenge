
# coding: utf-8

# PyPoll

# In[ ]:


# The goal of this project is to analyze the votes and calculate the following:
# Total number of votes cast
# Complete list of candidates who recieved votes
# The percentage of votes each candidate won
# The winner of the election based on popular vote
# print analysis to the terminal AND export to a text file


# In[ ]:


# import libraries
# create file paths across operating systems
import os
# module for reading CSV files
import csv
import pandas


# In[ ]:


# Read csv file, 
#PATH:  "C:\Users\maden\Documents\Data_Analytics_Boot_Camp2018\ExerciseDownload\UKED201808DATA5-master\03 - Python\Homework\Instructions\PyPoll\Resources\election_data.csv"


# In[ ]:


#Test the file - Open, print sample, then close
election_data = open("election_data.csv", "r+")
#Read the first row (header row) and next three rows
print(election_data.readline())
print(election_data.readline())
print(election_data.readline())
print(election_data.readline())
election_data.close()


# In[18]:


# reading csv file
filename = "election_data.csv"
# initialize titles and rows lists
fields = []
rows = []


#read csv file
with open(filename, 'r') as csvfile:
    # create a csv reader object
    csvreader = csv.reader(csvfile)
    # extract field names through first row
    fields = next(csvreader)
    # extract each data row one by one
    for row in csvreader:
        rows.append(row)
    # get total number of rows
    total_rows = csvreader.line_num - 1
    print("Total no. of rows: %d"%(total_rows))
    
    # print the field names
print('Field names are: ' + ', '.join(field for field in fields))

# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col, end = "")
    print('\n')
    


# In[19]:


# Total number of votes cast
total_votes = total_rows
print("Total Votes: %s" % total_votes)


# In[20]:


# candidates with votes
unique_candidates = []
for row in rows:
    if row[2] not in unique_candidates:
        unique_candidates.append(row[2])
print("Candidates who received votes: ")
print("-------------------------------")
print(*unique_candidates, sep = '\n')


# In[56]:


# Total and Percentage of Votes Each Candidate Won
Khan = 0
Correy = 0
Li = 0
OTooley = 0

for row in rows:
    if row[2] == "Khan":
        Khan = Khan + 1
    elif row[2] == "Correy":
        Correy = Correy + 1
    elif row[2] == "Li":
        Li = Li + 1
    elif row[2] == "O'Tooley":
        OTooley = OTooley + 1
        
print("POPULAR VOTE TOTALS and PERCENT:")
print("-------------------------")
print("Khan:     %.3f%% (%s)" % ((Khan/total_votes * 100),khan))
print("Correy:   %.3f%% (%s)" % ((Correy/total_votes * 100),Correy))
print("Li:       %.3f%% (%s)" % ((Li/total_votes),Li * 100))
print("O'Tooley: %.3f%% (%s)" % ((OTooley/total_votes * 100),OTooley))


# In[71]:


#Winner, Winner, Chicken, Dinner...
def winner():
    if Khan > Correy and Khan > Li and Khan > OTooley:
        return "Winner: Khan"
    elif Correy > Khan and Correy > Li and Correy > OTooley:
        return "Winner: Correy"
    elif Li > Correy and Li > Khan and Li > OTooley:
        return "Winner: Li"
    elif OTooley > Li and OTooley > Correy and OTooley > Khan:
        return "Winner: O'Tooley"
    else:
        return "Too Close to Call!"


# In[72]:


#Create a text file
pypolltxt = open("pypoll.txt", "w")
pypolltxt.write("ELECTION RESULTS \n")
pypolltxt.write("----------------------------------------------\n")
pypolltxt.write("Total Votes: %s" % total_votes + "\n")
pypolltxt.write("----------------------------------------------\n")
pypolltxt.write("POPULAR VOTE TOTALS and PERCENT:")
pypolltxt.write("-------------------------\n")
pypolltxt.write("Khan:     %.3f%% (%s)" % ((Khan/total_votes * 100),khan) + "\n")
pypolltxt.write("Correy:   %.3f%% (%s)" % ((Correy/total_votes * 100),Correy) + "\n")
pypolltxt.write("Li:       %.3f%% (%s)" % ((Li/total_votes),Li * 100) + "\n")
pypolltxt.write("O'Tooley: %.3f%% (%s)" % ((OTooley/total_votes * 100),OTooley) + "\n")
pypolltxt.write("----------------------------------------------\n")
pypolltxt.write(winner() + "\n")
pypolltxt.write("----------------------------------------------\n")


# In[73]:


# close the text file
pypolltxt.close()

