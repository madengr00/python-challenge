
# coding: utf-8

# import budget_data.csv
# The dataset contains 2 columns, Date and Profit / Losses

# In[1]:


# create file paths across operating systems
import os
# module for reading CSV files
import csv
import pandas as pd


# In[39]:


# This is the hard way to import a csv
'''csvpath = os.path.join("..","Module-3","budget_data.csv")
with open (csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:
        print(row)'''
# I like to use pandas... It is so much cleaner and simpler #Savemysanity
csvpath = pd.read_csv("budget_data.csv")
print(csvpath.head(10))


# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 
# 
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# In[40]:


#Calculate Total Months of Data
total_months = csvpath['Date'].count()
print("FINANCIAL ANALYSIS")
print("-----------------------------------")
print("Total Months: " + str(total_months))


# In[41]:


#Calculate TotalProfits / Losses
total_profit = csvpath['Profit/Losses'].sum()
print("Total: $" + str(total_profit))


# In[42]:


#Calculate Average Change
average_change = csvpath['Profit/Losses'].diff().mean()
print("Average Change: $" + str("%.2f" % average_change))


# In[43]:


#Calculate and Print the Greatest Increase in Profits
#Create a new column for the difference 
csvpath['dProfit/Losses'] = csvpath['Profit/Losses'].diff()
'''print(csvpath.head(5))'''
#Capture the date with the max difference in profits
print(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].max()])


# In[44]:


#Calculate and Print the Greatest Decrease in Profits
#Use the same difference column
#Capture the date with the min difference in profits
print(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].min()])


# In[45]:


#Create a text file
pybanktxt = open("pybank.txt", "w")


# In[46]:


#Print One last Time to Terminal - All Together
print("FINANCIAL ANALYSIS")
print("-----------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str("%.2f" % average_change))
print()
print("Greatest Increase in Profits: ")
print(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].max()])
print()
print("Greatest Decrease in Profits")
print(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].min()])


# In[47]:


#Write to a text file
pybanktxt.write("FINANCIAL ANALYSIS\n")
pybanktxt.write("-----------------------------------\n")
pybanktxt.write("Total Months: " + str(total_months) + "\n")
pybanktxt.write("Total: $" + str(total_profit) + "\n")
pybanktxt.write("Average Change: $" + str("%.2f" % average_change) + "\n")
pybanktxt.write("_________________________________\n")
pybanktxt.write("Greatest Increase in Profits: \n")
pybanktxt.write(str(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].max()]) + "\n")
pybanktxt.write("_________________________________\n")
pybanktxt.write("Greatest Decrease in Profits: \n")
pybanktxt.write(str(csvpath[['Date', 'dProfit/Losses']][csvpath['dProfit/Losses'] == csvpath['dProfit/Losses'].min()]) + "\n")


# In[48]:


# close the text file
pybanktxt.close()

