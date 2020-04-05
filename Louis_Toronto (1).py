#!/usr/bin/env python
# coding: utf-8

# # Louis - Segmenting and Clustering Neighborhoods in Toronto

# #### 1. Get the data from the webpage and transform it into a dataframe

# In[1]:


import pandas as pd
df=pd.read_html("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")[0]
df.head()


# #### 2. Dropping the rows for which a Borough is not assigned

# In[2]:


df = df[df.Borough != 'Not assigned']
df = df.reset_index(drop=True)
df.head()


# #### Combining rows for Postal codes that have different neighborhoods

# In[5]:


df2 = df.groupby(by=['Postal code','Borough']).agg(lambda x: ','.join(x))
df2.reset_index(level=['Postal code','Borough'], inplace=True)
df2.head()


# #### Define Not assigned Neighborhoods to be same as Borough

# In[6]:


df3=df2[df2.Borough != 'Not assigned']
df3.head()


# #### Print then number of rows in the dataframe

# In[8]:


print(df3.shape[0])


# In[ ]:




