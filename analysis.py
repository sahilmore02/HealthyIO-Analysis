import mysql.connector
import pandas as pd

# Replace this with your own credentials
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="healthyIO"
) 

query = "select * from user"
user = pd.read_sql(query, conn)

query = "select * from profile"
profile = pd.read_sql(query, conn)

query = "select * from health_score"
health_score = pd.read_sql(query, conn)

query = "select * from physical_exercise"
physical_exercise = pd.read_sql(query, conn)

query = "select * from food_intake"
food_intake = pd.read_sql(query, conn)

print('-------------------------------------------------------')


#sleep vs health score
print('SLEEP vs HEALTH SCORE')
a = pd.merge(physical_exercise,health_score,how="inner",on="log_id")
a = a.rename(columns={'sleep_hours':'sleep(hr)'})
print(a.groupby('sleep(hr)')['score'].mean().sort_values(ascending=False))
print('-------------------------------------------------------')




#exercise type vs health score
print('EXERCISE TYPE vs HEALTH SCORE')
a = pd.merge(physical_exercise,health_score,how="inner",on="log_id")
a = a.rename(columns={'exercise_type':'exercise'})
print(a.groupby('exercise')['score'].mean().sort_values(ascending=False))
print('-------------------------------------------------------')



#calories burn vs health score
print('CALORIES BURN vs HEALTH SCORE')
a = pd.merge(physical_exercise,health_score,how="inner",on="log_id")
a['calories'] = pd.cut(
    a['calories_burn'],
    bins=[0,100,200,300,400],
    labels=['0 to 100','101 to 200','201 to 300','301 to 400']
)
print(a.groupby('calories')['score'].mean())
print('-------------------------------------------------------')



#water intake vs health score
print('WATER INTAKE vs HEALTH SCORE')

a = pd.merge(food_intake,health_score,how="inner",on="log_id")
a = a.rename(columns={'water_intake':'water(l)'})

a['water(ltr)'] = pd.cut(
    a['water(l)'],
    bins=[0,1,2,3,4],
    labels=['0-1 ltr','1-2 ltr','2-3 ltr','3-4 ltr']
)
print(a.groupby('water(ltr)')['score'].mean().sort_values(ascending=False))
print('-------------------------------------------------------')



#age groups vs health score
print('AGE GROUPS vs HEALTH SCORE')
profile['agegrps'] = pd.cut(
profile['age'],
bins=[0,18,30,60,100],
labels=['0 to 18','19 to 30','31 to 60', 'Above 60']
)

a = pd.merge(profile,health_score,how='inner',on='user_id')
a = pd.merge(a,user,how='inner',on='user_id')
print(a.groupby('agegrps')['score'].mean())
print("-------------------------------------------------------")
