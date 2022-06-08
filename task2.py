#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


data = pd.read_csv('casestudy.csv')
data


# In[34]:


for year in [2015,2016,2017]:
    print(20*'-')
    print(f"Total revenue of {year}:{data[data['year']==year]['net_revenue'].sum():.2f}")
    if year!=2015:
        print(f"Total customers current year {year}:{data[data['year']==year]['net_revenue'].sum():.2f}")
        print(f"Total customers previous year {year-1}:{data[data['year']==year-1]['net_revenue'].sum():.2f}")
        
        prev = data[data['year']==year-1]['customer_email']
        current = data[data['year']==year]['customer_email']
        new_customers = len(list(set(current).difference(prev)))
        new_ids = list(set(current).difference(prev))
        print(f'New customers year {year}: {new_customers}')
        lost_customers = len(list(set(prev).difference(current)))
        lost_ids = list(set(prev).difference(current))
        print(f'Lost customers year {year}: {lost_customers}')
        
        print(f"Revenue from new customers for year {year}              {data[data['customer_email'].isin(new_ids)]['net_revenue'].sum():.2f}")
        print(f"Revenue from lost customers for year {year}              {data[data['customer_email'].isin(lost_ids)]['net_revenue'].sum():.2f}")
        print(f"Existing growth for year {year}:              {data[data['year']==year]['net_revenue'].sum()-data[data['year']==year-1]['net_revenue'].sum():.2f}")
    print(20*'-')
    


# In[40]:


import  matplotlib.pyplot as plt

total_revenue = data.groupby(by='year')[['year','net_revenue']].sum()
plt.figure(figsize=(10,10))
plt.title('Total revenue each year')
sns.barplot(x='year',y='net_revenue',data=total_revenue)
plt.show()


# In[42]:


# Check what mail customers use
data['mail'] = data['customer_email'].apply(lambda x:x.split('@')[1])
data['mail'].value_counts()

