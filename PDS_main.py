#---pocketDataAnalist---- #*https://www.kaggle.com/code/tanmay111999/heart-failure-prediction-cv-score-90-5-models
#*data summarize
#*Data Analysis(Checking for outliers, https://www.kaggle.com/code/madhurpant/heart-disease-eda)
#    options:
#     -compare variables
#     -corelation
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

#*data cleaining
#-ponerle dos temas 
#
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
pd.options.display.float_format = '{:.2f}'.format
import warnings
warnings.filterwarnings('ignore')

colors = ['#F93822','#FDD20E']

data = pd.read_csv('heart.csv')

col = list(data.columns)
categorical_features = []
numerical_features = []
for i in col:
    if len(data[i].unique()) > 6:
        numerical_features.append(i)
    else:
        categorical_features.append(i)

print('Categorical Features :',*categorical_features)
print('Numerical Features :',*numerical_features)



from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df1 = data.copy(deep = True)

# df1['Sex'] = le.fit_transform(df1['Sex'])
# df1['ChestPainType'] = le.fit_transform(df1['ChestPainType'])
# df1['RestingECG'] = le.fit_transform(df1['RestingECG'])
# df1['ExerciseAngina'] = le.fit_transform(df1['ExerciseAngina'])
# df1['ST_Slope'] = le.fit_transform(df1['ST_Slope'])
# fig, ax = plt.subplots(nrows = 3,ncols = 2,figsize = (10,15))
# for i in range(len(numerical_features) - 1):
#     plt.subplot(3,2,i+1)
#     ax = sns.countplot(numerical_features[i],data = data,hue = "HeartDisease",palette = colors,edgecolor = 'black')
#     for rect in ax.patches:
#         ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2, rect.get_height(), horizontalalignment='center', fontsize = 11)
#     title = numerical_features[i] + ' vs HeartDisease'
#     plt.legend(['No Heart Disease','Heart Disease'])
#     plt.title(title);
# for col in data.columns:

#     df1[col] = le.fit_transform(df1[col])


# fig, ax = plt.subplots(nrows = 3,ncols = 2,figsize = (10,15))
# for i in range(len(categorical_features) - 1):
    
#     plt.subplot(3,2,i+1)
#     sns.distplot(df1[categorical_features[i]],kde_kws = {'bw' : 1},color = colors[0]);
#     title = 'Distribution : ' + categorical_features[i]
#     plt.title(title)
    
# plt.figure(figsize = (4.75,4.55))

# sns.distplot(df1[categorical_features[len(categorical_features) - 1]],kde_kws = {'bw' : 1},color = colors[0])
# title = 'Distribution : ' + categorical_features[len(categorical_features) - 1]
# plt.title(title);

a = 0
fig,ax = plt.subplots(nrows = 5,ncols = 2,figsize = (15,25))
for i in range(len(numerical_features)):
    for j in range(len(numerical_features)):
        if i != j and j > i:
            a += 1
            plt.subplot(5,2,a)
            sns.scatterplot(x = numerical_features[i],y = numerical_features[j],data = data,hue = 'HeartDisease',palette = colors, edgecolor = 'black');
            plt.legend(['No Heart Disease', 'Heart Disease'])
            title = numerical_features[i] + ' vs ' + numerical_features[j]
            plt.title(title)
# values = data["Sex"].value_counts()
# plt.pie(values, labels=["male","female"], explode=(0,0.1), autopct="%.2f%%", startangle=56)
# 

# print(pd.unique(data["RestingECG"]))

# values = data["RestingECG"].value_counts()
# dlist = pd.unique(data["RestingECG"])
# plt.pie(values, labels=dlist, autopct="%.2f%%", startangle=56)
plt.show()


