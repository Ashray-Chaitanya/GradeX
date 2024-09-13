import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('GradeX/1BI22IS31.csv')
x = data["Subject"]
y = data["Total" ]
plt.pie(y,labels=x,autopct='%1.lf%%')
plt.title("jod")
plt.show()


