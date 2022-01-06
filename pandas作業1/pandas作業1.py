import pandas as pd

df1 = pd.read_csv('甲班.csv',encoding="big5", sep=",")

print(df1)

#df1.columns =['國文','英文','數學','歷史','理化','總分']

df1.insert(7, column="總分", value="0")
df1.head()
df1['總分'] =  df1[['國文','英文','數學','歷史','理化']].sum(1)

print(df1)

df1_sort = df1.sort_values(by=['總分'])
#df.sort_values(by=['col1'])
print(df1_sort)

En_good = df1['英文']>=60
Ma_good = df1['數學']>=60
print(En_good & Ma_good )