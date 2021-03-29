# -*- coding: utf-8 -*-
"""Mulitple Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XpqXl_P3koVhXlVVTwSCSDoyLX3WVRqQ
"""

# Commented out IPython magic to ensure Python compatibility.
# to know more about these package see, simple linear regression
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
# %matplotlib inline

from google.colab import files
#uploading dataset
uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

df = pd.read_csv("dataSet.csv")

# take a look at the dataset
df.head()

"""Lets select some features that we want to use for regression.

"""

cdf = df[['sqrt',	'washRoom',	'bedRoom',	'floor',	'lift',	'roadSize','areaIndex','SalePrice']]
cdf.tail(9)

msk = np.random.rand(len(df)) < 1
train = cdf[msk]
test = cdf[~msk]

print (train)

from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['sqrt',	'washRoom',	'bedRoom',	'floor',	'lift',	'roadSize','areaIndex']]) # here is the difference from simple regression
y = np.asanyarray(train[['SalePrice']])
regr.fit (x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)

import joblib

filename= 'Finalized_model.sav'
joblib.dump(regr,filename)

"""<h2 id="prediction">Prediction</h2>

"""

regr.predict(np.array([[2000,3, 4,4,1,20,3]]))