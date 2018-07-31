import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree,svm



df=pd.read_csv('PerpData1.csv')

features=list(df.columns[1:6])
y=df['Hired']
x=df[features]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)



def logisReg(a,b,c,d,e):
    model=LogisticRegression()
    model.fit(x,y)
    return (model.predict([[a,b,c,d,e]])[0])
    
def deciReg(a,b,c,d,e):
    model=tree.DecisionTreeClassifier()
    model=model.fit(x,y)
    return (model.predict([[a,b,c,d,e]])[0])

def randfor(a,b,c,d,e):
    clf=RandomForestClassifier(n_estimators=10)
    clf=clf.fit(x,y)
    return (clf.predict([[a,b,c,d,e]])[0])

def svmReg(a,b,c,d,e):
    clf=svm.SVC(kernel='linear',C=2.0).fit(x,y)
    return (clf.predict([[a,b,c,d,e]])[0])

def finalM(n,a,b,c,d,e):
    global df
    df.loc[len(df)] = [n,a,b,c,d,e]
    df.to_csv('PerpData1.csv',encoding='utf-8', index=False)
    
