from matplotlib import pyplot as plt

m = 420
xlist = []
wlist = []

eps = 0.3
a = 0.5
for ii in range(m):
    x = 0.001
    y = 0.02
    for i in range(2000):
        nx = 1 - a * x ** 2 + eps * (x - y)
        ny = 1 - a * y ** 2 + eps * (y - x)
        x = nx
        y = ny

    for k in range(500):
        nx = 1 - a * x ** 2 + eps * (x - y)
        ny = 1 - a * y ** 2 + eps * (y - x)
        xlist.append(ny)
        wlist.append(a)
        x = nx
        y = ny
    a = a + 0.0025

fig, ax = plt.subplots()
plt.xlabel('a')
plt.ylabel('x')
plt.xlim(0.25, 2)
plt.ylim(-1.5, 1.5)
ax.scatter(wlist, xlist, s = 1, color = "blue")
fig.set_figheight(8)
fig.set_figwidth(10)
plt.show()