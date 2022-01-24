#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("/home/root1/Downloads/Food-Truck-LineReg (1).csv")


# In[3]:


df.head()


# In[4]:


df.columns=["X","Y"]
df.head()


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


import seaborn as sns


# In[7]:


x,y=df["X"],df["Y"]
plt.scatter(x,y,alpha=0.6)
plt.title("scatter plot")
plt.xlabel("X->")
plt.ylabel("Y->")


# In[9]:


heatmap=sns.heatmap(df.corr(),annot=True)
df["Y"].corr(df["X"])


# In[10]:


Xsquare=[]
Ysquare=[]
XY=[]
for i in range(len(df)):
    Xsquare.append(round(df.X[i]**2,4))
    Ysquare.append(round(df.Y[i]**2,4))
    XY.append(round(df.Y[i]*df.X[i],4))
df["Xsquare"]=Xsquare
df["Ysquare"]=Ysquare
df["XY"]=XY
df.head()


# In[26]:


summ=0
sumX=0
sumY=0
suumX=0
suumY=0
xmean=0
ymean=0
for i in range(len(df)):
    summ=summ+XY[i]
    sumX=sumX+Xsquare[i]
    sumY=sumY+Ysquare[i]
    suumX=suumX+df.X[i]
    suumY=suumY+df.Y[i]
print(summ)
print(sumX)
print(sumY)
xmean=suumX/len(df)
ymean=suumY/len(df)
print(xmean)
print(ymean)
r=summ/(sumX*sumY)
print(r)


# In[30]:


import math
sdx=0
sdy=0
for i in range(len(df)):
    valx=df.X[i]
    valy=df.Y[i]
    sdx=sdx+((valx-xmean)*(valx-xmean))
    sdy=sdy+((valy-ymean)*(valy-ymean))
sdx=sdx/len(df)
sdy=sdy/len(df)
sdx=math.sqrt(sdx)
sdy=math.sqrt(sdy)
print(sdx)
print(sdy)


# In[32]:


m=(sdy/sdx)*r
print(m)


# In[33]:


c=ymean-(m*xmean)
print(c)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
