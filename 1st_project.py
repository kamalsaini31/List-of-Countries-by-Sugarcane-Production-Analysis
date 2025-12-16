# import necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generator function for file processing

df=pd.read_csv("List-of-Countries-by-Sugarcane-Production.csv")
df

"""**DATA** **CLEANING**"""

df.head(10)

df.nunique()

df.shape

df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_').str.replace('(','')
df.columns=df.columns.str.replace(')','')

df.columns

df.dtypes

df['production_tons'] = df['production_tons'].str.replace('.', '', regex=False).astype(float)
df['production_per_person_kg'] = df['production_per_person_kg'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
df['acreage_hectare'] = df['acreage_hectare'].str.replace('.', '', regex=False).astype(float)
df['yield_kg_/_hectare'] = df['yield_kg_/_hectare'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

df.drop("unnamed:_0",axis=1,inplace=True)

df.isnull().sum()
df[df['acreage_hectare'].isnull()]

df=df.dropna().reset_index(drop=True)

"""ANALYSIS

HOW MANY COUNTRIES PRODUCE SUGARCANE FROM EACH CONTINENT
"""

df['continent'].value_counts()

df['continent'].value_counts().plot(kind='bar')
plt.xlabel('continent')

"""DATA DESCRIBE

"""

df.describe()

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
sns.boxplot(df['production_tons'])
plt.title('production_tons')
plt.subplot(2,2,2)
sns.boxplot(df['production_per_person_kg'])
plt.title('production_per_person_kg')
plt.subplot(2,2,3)
sns.boxplot(df['acreage_hectare'])
plt.title('acreage_hectare')
plt.subplot(2,2,4)
sns.boxplot(df['yield_kg_/_hectare'])
plt.title('yield_kg_/_hectare')

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
sns.distplot(df['production_tons'])
plt.title('production_tons')
plt.subplot(2,2,2)
sns.distplot(df['production_per_person_kg'])
plt.title('production_per_person_kg')
plt.subplot(2,2,3)
sns.distplot(df['acreage_hectare'])
plt.title('acreage_hectare')
plt.subplot(2,2,4)
sns.distplot(df['yield_kg_/_hectare'])
plt.title('yield_kg_/_hectare')

sns.violinplot(x='continent',y='production_tons',data=df)
#

sns.violinplot(df['production_tons'])

"""Which country produce maximum sugracane continent wise?"""

df_africa=df[df['continent']=='Africa']
df_africa.sort_values('production_tons',ascending=False)

df_asia=df[df['continent']=='Asia']
df_asia.sort_values('production_tons',ascending=False)

df_europe=df[df['continent']=='Europe']
df_europe.sort_values('production_tons',ascending=False)

df_north_america=df[df['continent']=='North America']
df_north_america.sort_values('production_tons',ascending=False)

df_south_america=df[df['continent']=='South America']
df_south_america.sort_values('production_tons',ascending=False)

df_oceania=df[df['continent']=='Oceania']
df_oceania.sort_values('production_tons',ascending=False)

df['prod_per%']=(df['production_tons']/df['production_tons'].sum())*100
df.sort_values('prod_per%',ascending=False)

"""Which country has highest production ?"""

sorted_production_tons=df[['country','production_tons']].sort_values('production_tons',ascending=False)
sorted_production_tons["per%"]=(sorted_production_tons['production_tons']/sorted_production_tons['production_tons'].sum())*100
sorted_production_tons.head()
top_5=sorted_production_tons.iloc[0:5,:]
top_5
other_countries=sorted_production_tons.iloc[5:,:]
other_per=other_countries['per%'].sum()
top_6=top_5._append({'country':'Other','production_tons':other_countries['production_tons'].sum(),'per%':other_per},ignore_index=True)
plt.pie(top_6['per%'],labels=top_6['country'],autopct='%1.1f%%')

"""Correlation"""

df.corr(numeric_only=True)

plt.figure(figsize=(4,3))
sns.heatmap(df.corr(numeric_only=True),annot=True)

"""Do countries with highest land produce more sugarcane ?"""

plt.figure(figsize=(4,3))
plt.scatter(df['acreage_hectare'],df['production_tons'])
plt.xlabel('acreage_hectare')
plt.ylabel('production_tons')

"""**Do countries which yield more sugarcane per hactare produces more sugarcane in total ?**"""

plt.figure(figsize=(4,3))
plt.scatter(df['yield_kg_/_hectare'],df['production_tons'])
plt.xlabel('yield_kg_/_hectare')
plt.ylabel('production_tons')

sns.scatterplot(data=df,x='yield_kg_/_hectare',y='production_tons',hue='continent')

"""**Analysis** **for** **Continent**"""

df_continent=df.groupby('continent').sum()
df_continent.head()
df_continent['number_of_countries']=df.groupby('continent').count()['country']
df_continent

"""Which continent produces maximum sugarcane ?"""

df_continent['production_tons'].sort_values(ascending=False).plot(kind='bar')

df_continent['number_of_countries'].sort_values(ascending=False).plot(kind='bar')

df_continent['acreage_hectare'].sort_values(ascending=False).plot(kind='bar')

df_continent['production_per_person_kg'].sort_values(ascending=False).plot(kind='bar')

