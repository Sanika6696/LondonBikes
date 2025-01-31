#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install zipfile')


# In[2]:


get_ipython().system('pip install kaggle')


# In[3]:


import zipfile


# In[6]:


import pandas as pd
import kaggle


# In[10]:


# Download dataset from kaggle using Kaggle API 
# -d is for specifying the dataset

get_ipython().system('kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset')


# In[16]:


# extract file from the downloaded zip file 

import zipfile

zipfile_name = 'london-bike-sharing-dataset.zip'

# Extract the file
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()


# In[19]:


import numpy
bikes = pd.read_csv("london_merged.csv")


# In[ ]:


get_ipython().system('pip uninstall numpy')


# In[1]:


get_ipython().system('pip install numpy')


# In[2]:


get_ipython().system('pip show numpy pandas')


# In[3]:


get_ipython().system('pip show pandas')


# In[1]:


import numpy as np
import pandas as pd


# In[2]:


get_ipython().system('pip install --upgrade bottleneck')


# In[3]:


bikes = pd.read_csv("london_merged.csv")


# In[4]:


bikes.info


# In[5]:


bikes.head(5)


# In[6]:


bikes.shape


# In[7]:


bikes


# In[8]:


# count the unique values in weather_code column

bikes.weather_code.value_counts()


# In[9]:


# count the unique values in season

bikes.season.value_counts()


# In[10]:


new_col_dict = {
    'timestamp':'time',
    'cnt':'count',
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the cols to the specified col names, inTrue helps rename in the old dataset
# if not inPlace we can store it in new dataset with changed names

bikes.rename(new_col_dict, axis=1, inplace=True)


# In[11]:


bikes


# In[12]:


#changing the humidity percent value to percentage (i.e. a value between 0 and 1)

bikes.humidity_percent = bikes.humidity_percent/100
bikes.humidity_percent


# In[14]:


#creating a season dictionary so that we can map the integers 0-3 to the actual written values

season_dict = {
    '0.0' : 'spring',
    '1.0' : 'summer',
    '2.0' : 'autumn',
    '3.0' : 'winter',
}

# creating a weather dictionary so that we can map the integers to actual written values

weather_dict = {
    '1.0' : 'Clear',
    '2.0' : 'Scattered clouds',
    '3.0' : 'Broken clouds',
    '4.0' : 'Cloudy',
    '7.0' : 'Rain',
    '10.0' : 'Rain with thunderstrom',
    '26.0' : 'Snowfall',
}

# changing the season col datatypes as string
bikes.season = bikes.season.astype('str')

# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

bikes.season


# In[15]:


# changing the datatype of weather to string

bikes.weather = bikes.weather.astype('str')

# mapping the values to the actual weather 

bikes.weather = bikes.weather.map(weather_dict)

bikes.weather


# In[16]:


bikes.head()


# In[17]:


bikes.to_excel('london_bikes_final_sheet.xlsx', sheet_name='Data')


# In[ ]:





# In[ ]:




