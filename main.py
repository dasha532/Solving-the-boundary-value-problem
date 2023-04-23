import math
import matplotlib.pyplot as plt


a = 0
b = 1
n = 10
h = (b - a) / n
x = (n + 1) * [0]
y = (n + 1) * [0]
alpha = (n + 1) * [0]
betta = (n + 1) * [0]
y_new = (n + 1) * [0]
for i in range(0, n + 1):
    x[i] = round((a + i * h), 4)

for i in range(0, n + 1):
    y[i] = round((-1.5 * math.e ** (2 * x[i]) + 1.25 * math.e ** (4 * x[i]) + 1.25), 4)

f = 10
p = -6
q = 8
A = 1
B = round((-1.5 * math.e ** 2 + 1.25 * math.e ** 4 + 1.25), 4)
ap = 1 / h ** 2 - p / (2 * h)
bp = -2 / h ** 2 + q
cp = 1 / h ** 2 + p / (2 * h)
kappa1 = 0
mu1 = A
kappa2 = 0
mu2 = B
# Прямой ход
alpha[1] = kappa1
betta[1] = mu1
for i in range(1, n):
    alpha[i + 1] = round((-cp/(ap*alpha[i] + bp)), 4)
    betta[i + 1] = round(((f - ap*betta[i])/(ap*alpha[i] + bp)), 4)

y_new[n] = B
y_new[0] = A
for i in range(n - 1, 0, -1):
    y_new[i] = round((alpha[i + 1]*y_new[i + 1] + betta[i + 1]), 4)

print(f'x[j]  y[j]  y_new[j]')
for j in range(0, n+1):
    print(f'{x[j]}, {y[j]},   {y_new[j]}')

a = plt.plot(x, y, color = 'r', label = 'Аналитический')
b = plt.plot(x, y_new, color = 'g', label = 'Численно')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()




