import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.special import expit

df = pd.read_csv("Student-University.csv", header = None)

df.head()

#X = list(df[0])
X = df.iloc[:,0:2]
Y = list(df[2])

#print(X.max())
for i in range(len(X)):
    X[0] =  ( X[0] - X[0].min() ) / ( X[0].max() - X[0].min() ) 
    X[1] =  ( X[1] - X[1].min() ) / ( X[1].max() - X[1].min() ) 
X.head()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 111)

x1 = list(x_train[0])
x1_test = list(x_test[0])
x2 = list(x_train[1])
x2_test = list(x_test[1])

b = [1,0.5,0.5]
l_rate = 0.3
e = 2.71828

n = len(x1)

def grad_desc(b):
    p = []
    x = []
    a = 0
    for i in range(n):
        x.append(b[0] + b[1] * x1[i] + b[2] * x2[i])
        #print(x[i])
    for i in range(n):
        #print( expit(x[i]) )
        p.append( 1 / ( 1 + ( e ** ( -1 * x[i] ) ) ) )
    for j in range(3):
        for i in range(n):
            a = l_rate * (y_train[i] - p[i]) * (p[i]) * (1 - p[i])
            if(j == 1):
                a *= x1[i]
            if(j == 2):
                a *= x2[i]
            b[j] += a 
        #print(b[j])
    return b

for i in range(5):
    b = grad_desc(b)
    #print(b[0])
print(b)

x = []
pred = []
nt = len(x_test)

for i in range(nt):
    x.append(b[0] + b[1] * x1_test[i] + b[2] * x2_test[i])
for i in range(nt):
    pred.append( 1 / ( 1 + ( e ** ( -1 * x[i] ) ) ) )
    
#print(pred)
for i in range(nt):
    if (pred[i] > 0.5):
        pred[i] = 1
    else:
        pred[i] = 0
print(pred)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))