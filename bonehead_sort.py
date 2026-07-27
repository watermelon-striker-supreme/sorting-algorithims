from matplotlib import pyplot as plt
import random

quantity = 20
n = 0
data = random.sample(range(1, quantity+1), quantity)
x_values = range(1, len(data) + 1)
plt.ion()

while True:

    plt.clf()
    colors = ['b'] * quantity
    colors[n] = 'r'
    plt.bar(x_values, data, color=colors)
    plt.xticks(range(1, len(data) + 1))
    plt.yticks(range(0, len(data)+ 1, 5))
    plt.pause(0.01)

    if n == len(data) - 1:
        break

    if data[n] > data[n+1]:
        z = abs(data[n] - data[n+1])
        data[n+1] += z
        data[n] -= z
        n = 0
    else:
        n += 1

plt.ioff()
plt.show()