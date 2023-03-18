import numpy as np

# Заданий вектор i
i = np.array([[6], [2], [1]])

# Матриця масштабування S
S = np.array([[1.5, 0, 0],
              [0, 2.7, 0],
              [0, 0, 1.0]])

# Матриця обертання R
angle = np.radians(15.0)
R = np.array([[np.cos(angle), -np.sin(angle), 0],
              [np.sin(angle), np.cos(angle), 0],
              [0, 0, 1]])

# Матриця переміщення T
T = np.array([[1.0, 0, 2.0],
              [0, 1.0, 2.0],
              [0, 0, 1.0]])

# Композитне матричне перетворення
M = np.dot(S, np.dot(R, np.dot(T, i)))

# Результат
j = M[:2]
print(j)
