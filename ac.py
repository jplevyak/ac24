#!/usr/bin/env python3

X = []
Y = []
for l in open("1", "r").readlines():
    x,y = l.strip().split()
    X.append(int(x))
    Y.append(int(y))
X = sorted(X)
Y = sorted(Y)
t = 0
for i in range(0, len(X)):
    t += abs(X[i] - Y[i])
print('1a', t)

t = 0
i, j = 0, 0
while i < len(X) and j < len(Y):
    if X[i] == Y[j]:
        t += X[i]
        j += 1
    elif X[i] < Y[j]:
        i += 1
    else:
        j += 1
print('1b', t)

t = 0
for l in open("2", "r").readlines():
    x = l.strip().split()
    x = list(map(int, x))
    d = 0
    for i in range(0, len(x)-1):
       dd = x[i] - x[i+1]
       if abs(dd) > 3 or dd == 0 or d * dd < 0:
           break
       d = dd
       if i == len(x) - 2:
           t += 1
print('2a', t)

t = 0
for l in open("2", "r").readlines():
    x = l.strip().split()
    x = list(map(int, x))
    d = 0
    b = 0
    for i in range(0, len(x)-1):
       dd = x[i] - x[i+1]
       if abs(dd) > 3 or dd == 0 or d * dd < 0:
           if b > 0:
               break
           b += 1
       else:
           d = dd
       if i == len(x) - 2:
           t += 1
print('2b', t)
