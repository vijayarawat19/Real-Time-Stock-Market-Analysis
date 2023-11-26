#!/usr/bin/env python
# coding: utf-8

# In[16]:


from kafka import KafkaConsumer,KafkaProducer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem


# In[17]:


consumer = KafkaConsumer(
        'test',
        bootstrap_servers = ['43.204.115.188:9092'],
        value_deserializer = lambda x: loads(x.decode('utf-8'))
)


# In[ ]:





# In[ ]:


for c in consumer:
    print(c.value)


# In[18]:


pip install s3fs


# In[19]:


s3 = S3FileSystem()


# In[ ]:


for count, i in enumerate(consumer):
    with s3.open("s3://stock-market-vijaya/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)    


# In[ ]:


for count, i in enumerate(consumer):
    print(count)
    print(i.value)


# In[ ]:




