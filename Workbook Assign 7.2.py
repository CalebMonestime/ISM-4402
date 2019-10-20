#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
gender = ['Male','Female','Female''Male','Female']
status = ['Senior','Senior','Junior','Junior','Senior']
GradeList = zip(names,grades,status,gender)
df = pd.DataFrame(data = GradeList,columns=['Names','Grades','Status','Gender'])

df.boxplot(column='Grades')


# In[2]:


df.boxplot(by='Status', column='Grades')


# In[3]:


axisl = df.boxplot(by='Status', column='Grades')
axisl.set_ylim(50,110)


# In[ ]:




