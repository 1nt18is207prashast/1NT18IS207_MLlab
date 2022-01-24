#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd


# In[106]:


df=pd.read_csv("/home/root1/Downloads/zoo.data")


# In[107]:


df.head()


# In[108]:


df.info()


# In[109]:


df.shape


# In[112]:


x=df.iloc[:,1:17]


# In[113]:


y=df.iloc[:,17:]


# In[114]:


x.shape


# In[115]:


y.shape


# In[116]:


x


# In[117]:


y


# In[118]:


from sklearn.model_selection import train_test_split


# In[119]:


x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.8,test_size=0.2)


# In[120]:


from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(x_train, y_train)


# In[121]:


import matplotlib.pyplot as plt


# In[122]:


from sklearn import tree


# In[123]:


tree.plot_tree(clf);


# In[124]:


from sklearn.metrics import confusion_matrix


# In[125]:


pred = clf.predict(x_test)


# In[126]:


print(confusion_matrix(y_test,pred))


# In[127]:


accuracy=clf.score(x_test,y_test)


# In[128]:


print("accuracy:",accuracy)


# In[129]:


from sklearn.metrics import classification_report


# In[130]:


print(classification_report(y_test, pred))


# In[ ]:
