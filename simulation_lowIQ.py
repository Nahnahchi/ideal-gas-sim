from random import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot


npart = 100     # к-во молекул
nsteps = 10000  # к-во шагов
dt = 0.001      # время, проходящее за 1 шаг
rnd = lambda: 1.99 * (random() - 0.5)    # случайное число в интервале (-1;+1)
X = []          # список координат молекул по оси X
Y = []          # список координат по Y
Z = []          # список координат по Z
dX = []         # список скоростей всех молекул по X
dY = []         # список скоростей по Y
dZ = []         # список скоростей по Z


if __name__ == '__main__':

    # заполнить списки случайными числами
    for _ in range(npart):
        X.append(random())
        for i in Y, Z, dX, dY, dZ:
            i.append(rnd())

    # совершить nsteps шагов
    for n in range(nsteps):
        # рассмотреть каждую частицу
        for i in range(npart):
            # изменить направление (вектор скорости) частицы, если та зашла за пределы контейнера
            if abs(X[i] + dt * dX[i]) >= 1:
                dX[i] = -dX[i]
            if abs(Y[i] + dt * dY[i]) >= 1:
                dY[i] = -dY[i]
            if abs(Z[i] + dt * dZ[i]) >= 1:
                dZ[i] = -dZ[i]

            # рассчитать новые координаты
            X[i] = X[i] + dt * dX[i]
            Y[i] = Y[i] + dt * dY[i]
            Z[i] = Z[i] + dt * dZ[i]

    # вывести результаты
    v = 0
    for i in range(npart):
        v = v + pow(dX[i], 2) + pow(dY[i], 2) + pow(dZ[i], 2)
    print('v = %.2f' % v)
    fig = pyplot.figure()
    ax = pyplot.axes(projection='3d')
    ax.scatter3D(X, Y, Z)
    pyplot.show()
