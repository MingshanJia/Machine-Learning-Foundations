#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def make_data(n_samples=100):
    rnd = np.random.RandomState(42)
    x = rnd.uniform(1, 7, size=n_samples)
    y_no_noise = (np.sin(4 * x) + x + 5)
    y = (y_no_noise + rnd.normal(size=len(x))) / 2
    y *= 5
    return x.reshape(-1, 1), y


# In[ ]:




