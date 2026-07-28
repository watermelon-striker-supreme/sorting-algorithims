from matplotlib import pyplot as plt
import random

quantity = 20
data = random.sample(range(1, quantity+1), quantity)
x_values = range(1, len(data) + 1)
plt.ion()

n = 0

while True:

    plt.clf()
    colors = ['b'] * quantity
    colors[n] = 'r'
    plt.bar(x_values, data, color=colors)
    plt.xticks(range(1, len(data) + 1))
    plt.yticks(range(0, len(data)+ 1, 5))
    plt.pause(0.01)

    if n == 10:
        break

    if data[n] >= 11:
        a = int(data[n])
        data.pop(n)
        data.append(a)
        n -= 1

    n += 1

n = 0

while True:

    plt.clf()
    colors = ['b'] * quantity
    colors[n] = 'r'
    plt.bar(x_values, data, color=colors)
    plt.xticks(range(1, len(data) + 1))
    plt.yticks(range(0, len(data)+ 1, 5))
    plt.pause(0.01)

    if n == quantity-1:
        break

    if data[n] > data[n+1]:
        z = data[n] - data[n+1]
        data[n+1] += z
        data[n] -= z
        while True:
            if n == 0:
                break
            n -= 1
            if n == 0:
                break
            if data[n] < data[n-1]:
                x = data[n-1] - data[n]
                data[n-1] -= x
                data[n] += x
            else:
                break
    else:
        n += 1

plt.ioff()
plt.show()