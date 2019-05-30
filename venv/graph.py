from functions import *
import matplotlib.pyplot as plt
import math
from random import gauss

data = df("Road_Safety_Data.csv")

# # Bar chart

x = ['Fatal', 'Serious', 'Slight']
counts = [header_count('Accident_Severity', 1), header_count('Accident_Severity', 2), header_count('Accident_Severity', 3)]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, counts, color='green')
plt.title("Number of Accidents at each Severity Level")
plt.xticks(x_pos, x)
plt.show()
#######################################################################################
print('------------t-test example------------')
day_of_week = [row[9] for row in data]
casualties = [row[7] for row in data]
# combind into a 2d list
tData = [list(a) for a in zip(day_of_week, casualties)]
weekDaystr = [row[1] for row in tData if row[0]!='1' and row[0]!='7']
weekEndstr = [row[1] for row in tData if row[0]=='1' or row[0]=='7']
weekDay = [int(s) for s in weekDaystr]
weekEnd = [int(s) for s in weekEndstr]
print('Weekday mean casualties is', mean(weekDay))
print('Weekend mean casualties is', mean(weekEnd))
student_two(weekEnd, weekDay)
print('This large t value shows that the difference in these means is statistically significant')
# extract the data for each variable
speedLimits = [row[13] for row in data]
casualties = [row[7] for row in data]


#######################################################################################
print('------------ANOVA example------------')
# combind into a 2d list
anovaData = [list(a) for a in zip(speedLimits, casualties)]

# group the data. In this example we group by speed limit.

speed20str = [row[1] for row in anovaData if row[0]=='20']
speed30str = [row[1] for row in anovaData if row[0]=='30']
speed40str = [row[1] for row in anovaData if row[0]=='40']
speed20 = [int(s) for s in speed20str]
speed30 = [int(s) for s in speed30str]
speed40 = [int(s) for s in speed40str]

anova_one(speed20, speed30, speed40)
# F(2,33808) = 2.9957 for alpha = 0.05

