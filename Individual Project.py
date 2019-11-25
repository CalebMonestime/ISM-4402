#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[14]:


import matplotlib.pyplot as plt
import pandas as pd
CarsSold= [2,6,6,3,2]
HoursWorked = [39,46,42,38,33]
Lname= ['Walters', 'Henderson', 'Moore', 'Jackson', 'Sears']
HoursList= zip(CarsSold, HoursWorked, Lname)
df =pd.DataFrame(data = HoursList,
                columns=['Cars Sold', 'Hours Worked', 'Name'])
df2 = df.set_index(df['Name'])
get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')
df2.plot(kind="bar")


# In[25]:


import matplotlib.pyplot as plt
import pandas as pd
CarsSold= [3.76, 4.07]
Gender1= ['Female', 'Male']
Gender=zip(CarsSold, Gender1,)
df=pd.DataFrame(data=Gender,
               columns=['CarsSold','Gender1'])
df2=df.set_index(df['Gender1'])
get_ipython().magic(u'matplotlib inline')
df.plot(kind='bar')
df2.plot(kind="bar")


# In[ ]:





# In[ ]:




