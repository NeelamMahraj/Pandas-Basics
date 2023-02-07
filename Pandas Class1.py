#!/usr/bin/env python
# coding: utf-8

# # PANDAS BASICS 

# In[3]:


import pandas as pd

df = pd.DataFrame(
    {'name':["Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth"],
     'Age':[22, 35, 58],
     'Sex': ["male", "male", "female"],}
)
df

# <img src ='https://pandas.pydata.org/docs/_images/02_io_readwrite.svg'>


# <img src ='https://pandas.pydata.org/docs/_images/02_io_readwrite.svg'>
# 

# In[4]:


age = pd.Series([1,2,3,4],name='Age')
print(age)


# In[5]:


df['Age'].max()


# In[6]:


# Give statiscal summary
df['Age'].describe()


# In[8]:


#pandas data_range funtion

#df = pd.data_range(start= '2023-01-01',end= '2023-11-01')
per1 = pd.date_range(start ='1-1-2018', 
         end ='1-05-2018', freq ='5H')

per1


# In[9]:


import numpy as np
df = pd.DataFrame(np.arange(10*10).reshape(10,10))
df


# In[10]:


# matrix into dataframe
df = pd.DataFrame(np.arange(10*10).reshape(10,10),
                 columns= [chr(i) for i in range(65,65+10)])
df


# In[11]:


# create a dummy json file
df = pd.read_json('https://dummyjson.com/users')
df.head()


# In[12]:


# create a dummy excel file
df.to_excel('abc.xlsx')
df.head()


# In[13]:


# access specific column
# dataframe['columnname']
df.users


# In[14]:


# Give initial five elements of the dataset
df['total'].head()


# In[15]:


# Give Last five elements of the dataset
df['total'].tail()


# In[ ]:




