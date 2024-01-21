from matplotlib import pyplot as plt

def iter_2dim(init_cond, a, eps):

    x = 1 - a * (init_cond[0] ** 2) + eps * (init_cond[0] - init_cond[1])
    y = 1 - a * (init_cond[1] ** 2) + eps * (init_cond[1] - init_cond[0])

    return [x, y]

def phase_port(init_cond, a, eps):

    x1list = []
    y1list = []
    x2list = []
    y2list = []

    for i in range(1000):
        init_cond = iter_2dim(init_cond, a, eps)

    for j in range(10000):
        init_cond = iter_2dim(init_cond, a, eps)
        x1list.append(init_cond[0])
        y1list.append(init_cond[1])

    for j in range(5):
        init_cond = iter_2dim(init_cond, a, eps)
        x2list.append(init_cond[0])
        y2list.append(init_cond[1])

    return x1list, y1list, x2list, y2list

x0 = 0.001
y0 = 0.02

t = [x0, y0]
a1 = 1.37
eps1 = 0.26

portrait = phase_port(t, a1, eps1)

plt.figure(figsize = (13, 8))
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.scatter(portrait[0], portrait[1], s=0.3, color = 'black')
plt.show()