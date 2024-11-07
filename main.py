#importing matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
#reading csv file
rf=pd.read_csv("gappy.csv")
print(rf.info())
rf.isnull().any()
lables=['population','life_exp','gdp_cap']
for i in lables:
    sb.kdeplot(rf[i])
    plt.show()
sb.violinplot(data=rf,x='continent',y='life_exp',palette='viridis')
plt.show()