#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statsmodels.formula.api as sm

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


result = sm.ols(formula= 'grade ~ age - 1', data=df).fit()
result.summary()


# In[4]:


result = sm.ols(formula='grade ~ exercise - 1', data=df).fit()
result.summary()


# In[5]:


result = sm.ols(formula='grade ~ hours -1', data=df).fit()
result.summary()


# In[ ]:




