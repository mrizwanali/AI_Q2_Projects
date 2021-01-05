#!/usr/bin/env python
# coding: utf-8

# # Election Results
# 
# You’re part of an impartial research group that conducts phone surveys prior to local elections. During this election season, the group conducted a survey to determine how many people would vote for I_Khan vs. S_Sharif in the presidential election.
# 
# Now that the election has occurred, your group wants to compare the survey responses to the actual results.
# 
# Was your survey a good indicator? Let’s find out!

# # PROJECT STEPS

# 1.First, import numpy and matplotlib.

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# 2.There is a list given of the different survey responses.
# 
# Calculate the number of people who answered ‘I_Khan’ and save the answer to the variable total_Khan.
# 
# Print the variable to the terminal to see its value.

# In[4]:


survey_responses = ['I_Khan', 'S_Sharif', 'I_Khan', 'I_Khan', 'I_Khan','S_Sharif',
                    'S_Sharif', 'I_Khan', 'I_Khan', 'I_Khan', 'S_Sharif', 'S_Sharif',
                    'I_Khan', 'I_Khan', 'S_Sharif', 'S_Sharif','I_Khan', 'I_Khan', 
                    'S_Sharif', 'S_Sharif', 'S_Sharif', 'S_Sharif', 'S_Sharif', 'S_Sharif', 
                    'I_Khan', 'I_Khan', 'I_Khan', 'I_Khan', 'I_Khan', 'I_Khan',
                    'S_Sharif', 'S_Sharif', 'I_Khan', 'I_Khan', 'I_Khan', 'S_Sharif',
                    'S_Sharif', 'I_Khan', 'I_Khan', 'S_Sharif', 'S_Sharif', 'I_Khan', 
                    'I_Khan', 'S_Sharif', 'S_Sharif', 'S_Sharif', 'S_Sharif', 'S_Sharif',
                    'S_Sharif', 'I_Khan','S_Sharif', 'S_Sharif', 'I_Khan', 'I_Khan', 
                    'I_Khan', 'S_Sharif', 'S_Sharif', 'I_Khan', 'I_Khan', 'S_Sharif', 
                    'S_Sharif', 'I_Khan', 'I_Khan', 'S_Sharif', 'S_Sharif', 'S_Sharif', 
                    'S_Sharif', 'S_Sharif', 'S_Sharif', 'I_Khan']

#
total_Khan = survey_responses.count("I_Khan")
print(total_Khan)


# 3.Calculate the percentage of people in the survey who voted for I_Khan and save it to the variable percentage_I_Khan.
# 
# Print the variable to the terminal to see its value.

# In[5]:


percentage_I_Khan = (survey_responses.count("I_Khan") / len(survey_responses)) * 100
print(percentage_I_Khan)


# 4.In the real election, 54% of the 10,000 town population voted for I_Khan. Your supervisors are concerned because this is a very different outcome than what the poll predicted. They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.
# 
# Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters. Then divide the distribution by the number of survey responses. Save your calculation to the variable possible_surveys.
# 
# ######### hint###########
# possible_surveys = 
# np.random.binomial(total of survey responses, the actual success rate,and the size of the town’s population ) 

# In[18]:


possible_surveys = (np.random.binomial(len(survey_responses), 0.54, 10000)) / len(survey_responses)
print(possible_surveys)


# 
#       #######Optional########
# 5.By using matplotlib Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.
# 

# In[19]:


plt.hist(possible_surveys, bins = 20)
plt.show()


# 6.As we saw, 47% of people we surveyed said they would vote for I_Khan, but 54% of people voted for I_Khan in the actual election.
# 
# Calculate the percentage of surveys that could have an outcome of I_Khan receiving less than 50% of the vote and save it to the variable I_Khan_loss_surveys.
# 
# Print the variable to the terminal.

# In[ ]:


#type your code here


# 7.With this current poll, about 20% of the time a survey output would predict S_Sharif winning, even if I_Khan won the actual election.
# 
# Your co-worker points out that your poll would be more accurate if it had more responders.
# 
# Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. Divide the distribution by the size of the survey and save your findings to large_survey.
# 

# In[ ]:


#type your code here


# 8.Now, recalculate the percentage of surveys that would have an outcome of I_Khan losing and save it to the variable I_Khan_loss_new, and print the value to the terminal.
# 
# What do we notice about this new value?
# 
# What advice would you give to your supervisors about predicting results from surveys?
# 

# In[ ]:


#type your code here

