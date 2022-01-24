#!/usr/bin/env python
# coding: utf-8

# In[38]:


arr=[6,5,4,3,2]


# In[39]:


def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    
    return arr;


# In[40]:


bubblesort(arr)


# In[58]:


b=[13,24,31,2]


# In[59]:


bubblesort(b)


# In[60]:


n=len(b)


# In[61]:


sum=0
for i in range(n):
    sum+=b[i]
mean=sum/n
print(mean)


# In[62]:


if(n%2==0):
    print((b[n//2]+b[(n//2)-1])//2)
if(n%2!=0):
        print(b[n//2])


# In[63]:


a=[5,6,7,8,9]
n-len(a)
if(n%2==0):
    print((a[n//2]+a[(n//2)-1]/2))
else:
    print(a[n//2])


# In[64]:


import math
sum=0
for i in range(n):
    sum+=(b[i]-mean)**2
sd=print(math.sqrt(sum/2))


# In[67]:


#variance
sum=0
for i in range(n):
    sum+=(b[i]-mean)**2
variance=sum/n
print(float(variance))

