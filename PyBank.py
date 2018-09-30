
# coding: utf-8

# import budget_data.csv
# The dataset contains 2 columns, Date and Profit / Losses

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 
# 
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# In[7]:


# create file paths across operating systems
import os
# module for reading CSV files
import csv


# In[8]:


# This is the hard way to import and work with a csv - difficult to follow
budget_csv = os.path.join("..","Module-3","budget_data.csv")
with open (budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #skip / extract header row
    headers = next(csvreader)
    #empty lists for columns
    dates = []
    revenue = []
    #new column for difference in profits/losses
    rev_change = []
    # row by row
    for row in csvreader:
        #extract each date
        dates.append(row[0])
        #extract revenue for month
        revenue.append(float(row[1]))
        
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: ", len(dates))
    
    #Total Revenue - Net Profits / Losses
    total_revenue = sum(revenue)
    print("Total Revenue: $",total_revenue)
    
    # Total Net Profit / Loss
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        ''' be careful  "i-1" goes to end of the list'''
        avg_rev_change = sum(rev_change) / len(rev_change)
        max_change = max(rev_change)
        max_change_date = str(dates[rev_change.index(max(rev_change)) + 1])
        min_change = min(rev_change)
        min_change_date = str(dates[rev_change.index(min(rev_change)) + 1])
    ''' had to shift dates by 1 month to adjust for 1 month not having a diff.'''
    print("Average Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Profit: ", max_change_date, "($", max_change,")")
    print("Greatest Decrease in Profit: ", min_change_date, "($", min_change,")")

 


# In[12]:


#Create a text file
pybanktxt = open("pybank.txt", "w")


# In[13]:


#Write to a text file
pybanktxt.write("FINANCIAL ANALYSIS\n")
pybanktxt.write("-----------------------------------\n")
pybanktxt.write("Total Months: " + str(len(dates)) + "\n")
pybanktxt.write("Total Revenue: $" + str(total_revenue) + "\n")
pybanktxt.write("_________________________________\n")
pybanktxt.write("Average Revenue Change: $" + str(round(avg_rev_change)) + "\n")
pybanktxt.write("Greatest Increase in Profit: " +str(max_change_date) +  "  $" + str(max_change)+ "\n")
pybanktxt.write("Greatest Decrease in Profit: " +str(min_change_date) +  "  $" + str(min_change)+ "\n")


# In[14]:


# close the text file
pybanktxt.close()

