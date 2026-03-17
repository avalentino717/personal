# Made with help from https://www.kaggle.com/code/ahmetaslandev/basiclineerregressionimplement

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

df.isnull().sum()

df.drop('Unnamed: 0', axis=1, inplace=True)

sns.scatterplot(x="YearsExperience", y="Salary", data = df)
plt.xlabel("Years of Experience")
plt.title("Salary According to Experience")
#plt.show()

X = df[['YearsExperience']]
y = df['Salary']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_predict_test = lin_reg.predict(X_test)

r_score = r2_score(y_test, y_predict_test)

print(f"r2 score: {r_score}")

plt.scatter(X_train,y_train)
plt.plot(X_train, lin_reg.predict(X_train), color='red')
plt.show()