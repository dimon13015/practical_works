import numpy as np


def scaling(sx, sy, i):
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1.0]])
    return np.dot(S, i)


def rotation(theta, i):
    theta = np.radians(theta)
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    return np.dot(R, i)


def translation(tx, ty, i):
    T = np.array([[1.0, 0, tx],
                  [0, 1.0, ty],
                  [0, 0, 1.0]])
    return np.dot(T, i)


i1 = float(input("Введіть перший параметр вектору: "))
i2 = float(input("Введіть другий параметр вектору: "))
i = np.array([[i1], [i2], [1]])

a = i
operations = ['T', 'S', 'R']

for _ in range(3):
    op = input('Виберіть операцію: T, R, чи S\n').upper()
    while op not in operations:
        op = input('Виберіть операцію: T, R, чи S\n').upper()

    if op == 'S':
        sx = float(input('Масштабування - х: '))
        sy = float(input('Масштабування - у: '))
        a = scaling(sx, sy, a)

    if op == 'T':
        tx = float(input('Переміщення - x: '))
        ty = float(input('Переміщення - y: '))
        a = translation(tx, ty, a)

    if op == 'R':
        theta = float(input('Кут обертання: '))
        a = rotation(theta, a)

j = a[:2]
print("Результатом композитного матричного перетворення є:")
print(j)
