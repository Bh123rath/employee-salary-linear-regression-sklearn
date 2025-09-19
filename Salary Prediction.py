import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df=pd.read_excel('C:\\Users\\aaa\\Desktop\\expandsal.xlsx')
x=df[["Year of Experience"]]
y=df["salary"]
model=LinearRegression()
model.fit(x,y)
pred = model.predict([[6]])
print("Predicted Salary for 6 years:", pred[0])
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red')
plt.show()
