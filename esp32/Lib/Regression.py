from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

x=[10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
X=[[10], [8], [13], [9], [11] ,[14] ,[6], [4] ,[12], [7], [5]]
y=[8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

model = LinearRegression()
model.fit(X, y)
print('Bias: ', model.intercept_) #截距
print('Weight: ', model.coef_)      #斜率
y_pred = model.predict([[0], [1]])
print(y_pred) #x=0, x=1預測結果

xx=np.arange(0, max(x)+5, 0.1)
fx = model.coef_[0]*xx + model.intercept_

plt.scatter(x, y, label='data')
plt.legend()
plt.xlim(0, max(x)+5)
plt.xticks(np.arange(0, max(x)+5, step=1))
plt.ylim(0, model.coef_[0]*(max(x)+5) + model.intercept_)
plt.yticks(np.arange(0, model.coef_[0]*(max(x)+5) + model.intercept_, step=1))
plt.plot(xx, fx, '--r')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()