#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install kafka-python


# In[56]:


import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json


# In[57]:


producer = KafkaProducer(bootstrap_servers=['43.204.115.188:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


# In[42]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[43]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[47]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[48]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[49]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[50]:


producer.send('test', value={'surnasdasdame':'parasdasdmar'})


# In[51]:


producer.send('test', value={'Vijaya':'Rawat'})


# In[58]:


df = pd.read_csv("./diabetes.csv")


# In[53]:


df.head(10)


# In[ ]:


while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('test', value=dict_stock)
    sleep(1)


# In[ ]:




