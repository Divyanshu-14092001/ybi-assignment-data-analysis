#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv('Titanic.csv')


# In[3]:


titanic


# In[4]:


female = titanic[titanic['Sex'] == 'female']


# In[5]:


print(female.head(8))


# In[6]:


survived = female[female['Survived'] == 1].shape[0]
not_survived = female[female['Survived'] == 0].shape[0]


# In[7]:


print("Number of female passengers who survived:", survived)
print("Number of female passengers who did not survive:", not_survived)


# In[8]:


survived_by_class = female[female['Survived'] == 1].groupby('PassengerId').size()
not_survived_by_class = female[female['Survived'] == 0].groupby('PassengerId').size()


# In[9]:


print("Number of female passengers who survived by class:")
print(survived_by_class)


# In[10]:


print("\nNumber of female passengers who did not survive by class:")
print(not_survived_by_class)


# In[11]:


adult_passengers = titanic[titanic['Age'] > 18]


# In[12]:


print(adult_passengers)


# In[13]:


adult_female_passengers = titanic[(titanic['Age'] > 18) & (titanic['Sex'] == 'female')]


# In[14]:


print(adult_female_passengers)


# In[15]:


selected_passengers = titanic[(titanic['Age'] > 18) & (titanic['Sex'] == 'female') & (titanic['Pclass'] == 1)]


# In[16]:


print(selected_passengers)


# In[17]:


selected_passengers = titanic[(titanic['Age'] > 18) & (titanic['Sex'] == 'female') & (titanic['Pclass'] == 1)]


# In[18]:


mean_age = selected_passengers['Age'].mean()


# In[19]:


print("Mean age of selected passengers:", mean_age)


# In[20]:


selected_passengers = titanic[((titanic['Age'] > 18) | (titanic['Sex'] == 'female')) & (titanic['Pclass'] == 1)]


# In[21]:


print(selected_passengers)


# In[22]:


selected_passengers = titanic[(titanic['Age'] > 18) | ((titanic['Sex'] == 'female') & (titanic['Pclass'] == 1))]


# In[23]:


mean_age = selected_passengers['Age'].mean()


# In[24]:


print("Mean age of selected passengers:", mean_age)


# In[ ]:




