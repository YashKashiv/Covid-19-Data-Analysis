import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import seaborn as sn
import datetime as dt
import numpy as np

# use parse_dates method to convince pandas a specific column is in date format date

df=pd.read_csv('desktop/covid_19_india.csv',parse_dates=['Date'],dayfirst=True)

df.head()

#  Keeping only required columns
df=df[['Date','State/UnionTerritory','Cured','Deaths','Confirmed']]

# Renaming Column names
df.columns=['date','state','cured','deaths','confirmed']

df.head()

# Looking at latest dates or we can say 5 last records
df.tail()

today=df[df.date=='2021-08-11']

today.head()

# Sorting today's data to see most confirm cases in which state

max_confirmed_cases=today.sort_values(by='confirmed',ascending=False)
max_confirmed_cases.head()

# Getting 5 states with most confirmed cases
top_states_confirmed=max_confirmed_cases[0:5]

# USE sns.set METHOD TO SET SIZE
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x='state',y='confirmed',data=top_states_confirmed,hue='state')
plt.show()

max_death_cases=today.sort_values(by='deaths',ascending=False)
max_death_cases

top_states_death=max_death_cases[0:5]

sns.set(rc={'figure.figsize':(7,7)})
sns.barplot(x='state',y='deaths',data=top_states_death,hue='state')
plt.show()

max_cured_cases=today.sort_values(by='cured',ascending=False)
max_cured_cases.head()

top_states_cured=max_cured_cases[0:5]

sns.set(rc={'figure.figsize':(10,10)})
sns.barplot(x='state',y='cured',data=top_states_cured,hue='state')
plt.show()

maha=df[df.state=='Maharashtra']

maha.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=maha,color='r')
plt.show

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=maha,color='y')
plt.show

kerala=df[df.state=='Kerala']
kerala.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=kerala,color='r')
plt.show

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=kerala,color='y')
plt.show

jk=df[df.state=='Jammu and Kashmir']
jk.head()

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='confirmed',data=jk,color='r')
plt.show()

sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x='date',y='deaths',data=jk,color='y')
plt.show()