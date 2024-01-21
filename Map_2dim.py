import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

def iter_2dim(init_cond, a, eps):

    x = 1 - a * (init_cond[0] ** 2) + eps * (init_cond[0] - init_cond[1])
    y = 1 - a * (init_cond[1] ** 2) + eps * (init_cond[1] - init_cond[0])

    return [x, y]

def period_2dim(init_cond, a, eps, prd_complxty, err):

    for j in range(2000):
        init_cond = iter_2dim(init_cond, a, eps)
        if abs(init_cond[0]) > 100 or abs(init_cond[1]) > 100:
            return prd_complxty + 1

    var = iter_2dim(init_cond, a, eps)

    for i in range(prd_complxty):
        if np.sqrt((np.abs(var[0] - init_cond[0])) ** 2 + (np.abs(var[1] - init_cond[1])) ** 2) < err:
            return i+1
        else:
            var = iter_2dim(var, a, eps)
    return 0

#initial conditions
x0 = 0.001
y0 = 0.02

def prd_map_2dim(rows, cols, prd_complxty, x_left, x_right, y_down, y_up, err):
    ndarray = [[[x0, y0] for _ in range(rows)] for _ in range(cols)]
    array_colors = []
    array_x = []
    array_y = []
    l1 = []
    l2 = []
    common1 = []
    common2 = []
    list1 = np.linspace(x_left, x_right, rows)
    list2 = np.linspace(y_down, y_up, cols)

    for i in tqdm(range(rows)):
        for j in range(cols):
            period = period_2dim(ndarray[i][j], list1[i], list2[j], prd_complxty, err)
            array_colors.append(period)
            array_x.append(list1[i])
            array_y.append(list2[j])

    for g in range(prd_complxty + 2):
        for i in range(rows * cols):
            if array_colors[i] == g:
                l1.append(array_x[i])
                l2.append(array_y[i])
        common1.append(l1)
        common2.append(l2)
        l1 = []
        l2 = []

    return common1, common2

erg = prd_map_2dim(200, 200, 16, 1.04, 1.50, -0.7, 0.3, 0.001)

fig, ax = plt.subplots()
sizeOfPoint = 0.1
ax.scatter(erg[0][0], erg[1][0], label='Chaos', s=sizeOfPoint, color="black")
ax.scatter(erg[0][1], erg[1][1], label='Fixed', s=sizeOfPoint, color="blue")
ax.scatter(erg[0][2], erg[1][2], label='Period 2', s=sizeOfPoint, color="green")
ax.scatter(erg[0][3], erg[1][3], label='Period 3', s=sizeOfPoint, color="brown")
ax.scatter(erg[0][4], erg[1][4], label='Period 4', s=sizeOfPoint, color="red")
ax.scatter(erg[0][5], erg[1][5], label='Period 5', s=sizeOfPoint, color="purple")
ax.scatter(erg[0][6], erg[1][6], label='Period 6', s=sizeOfPoint, color="yellow")
ax.scatter(erg[0][7], erg[1][7], label='Period 7', s=sizeOfPoint, color="pink")
ax.scatter(erg[0][8], erg[1][8], label='Period 8', s=sizeOfPoint, color="orange")
ax.scatter(erg[0][9], erg[1][9], label='Period 9', s=sizeOfPoint, color="magenta")
ax.scatter(erg[0][10], erg[1][10], label='Period 10', s=sizeOfPoint, color="cyan")
ax.scatter(erg[0][11], erg[1][11], label='Period 11', s=sizeOfPoint, color="darkgreen")
ax.scatter(erg[0][12], erg[1][12], label='Period 12', s=sizeOfPoint, color="darkblue")
ax.scatter(erg[0][13], erg[1][13], label='Period 13', s=sizeOfPoint, color="gold")
ax.scatter(erg[0][14], erg[1][14], label='Period 14', s=sizeOfPoint, color="hotpink")
ax.scatter(erg[0][15], erg[1][15], label='Period 15', s=sizeOfPoint, color="navy")
ax.scatter(erg[0][16], erg[1][16], label='Period 16', s=sizeOfPoint, color="peru")
ax.scatter(erg[0][17], erg[1][17], label='Infinity', s=sizeOfPoint, color="gray")

ax.legend(loc='lower right', shadow=True, fontsize=8)

ax.set_title('Map of Regimes')
plt.xlabel('Parameter a')
plt.ylabel('Parameter eps')
fig.set_figheight(10)
fig.set_figwidth(10)
plt.show()
