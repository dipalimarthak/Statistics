###Outliers
#the values generally after 3rd standard deviation are outliers

import numpy as np
import matplotlib.pyplot as plt


## defining dataset

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
outliers=[]
#the values generally after 3rd standard deviation are outliers
#we can find outliers using z score

def detect_outliers(data):
    threshold=3 #standard deviations
    mean=np.mean(data)
    std=np.std(data)

    for i in data:
        z_score = (i-mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

# %%

plt.hist(dataset)
# %%

detect_outliers(dataset)


#IQR Inter Quartile Range
#1. I want to sort the data
#2. I will calculate Q1 (25 percentile) and Q3(75 percentile) 
#3. IQR =Q3-Q1
#4. Find the lower fence (Q1 - 1.5*IQR)
#4. Find the upper fence (Q3 + 1.5*IQR)

#sorting
dataset=sorted(dataset)
#Q1 and Q3 calculation
q1, q3 = np.percentile(dataset,[25,75])
print(q1,q3)

iqr=q3-q1
print(iqr)
#lower and higher fence
lower_fence= q1-(1.5 * iqr)
higer_fence= q3+(1.5 * iqr)
print(lower_fence,higer_fence)


#remove outliers

import seaborn as sns
sns.boxplot(dataset)