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

import re
t = 0
for x in re.findall('mul\(\d\d?\d?,\d\d?\d?\)', open("3", "r").read()):
  _, a, b, _  = re.split('\(|,|\)', x)
  t += int(a) * int(b)
print("3a", t)

t = 0
e = True
for x in re.findall('mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don\'t\(\)', open("3", "r").read()):
  if x.startswith('do'):
    e = x == 'do()'
    continue
  if e:
    _, a, b, _  = re.split('\(|,|\)', x)
    t += int(a) * int(b)
print("3b", t)

p = open("4", "r").readlines()

def get(x, y):
    if y < 0 or y >= len(p) or x < 0 or x >= len(p[y]):
        return None
    return p[y][x]

D = [(1, 0), (1, 1), (1, -1), (0, -1), (0, 1), (-1, 0), (-1, 1), (-1, -1)]
M = "MAS"
t = 0
for y in range(len(p)):
    for x in range(len(p[y])):
        if p[y][x] == 'X':
            for d in D:
                xx, yy = x, y
                found = True
                for m in M:
                    xx = xx + d[0]
                    yy = yy + d[1]
                    if get(xx, yy) != m:
                        found = False
                        break
                if found:
                    t += 1
print("4a", t)

D = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
M = ["MSMS", "MSSM", "SMSM", "SMMS"]
t = 0
for y in range(len(p)):
    for x in range(len(p[y])):
        if p[y][x] == 'A':
            for mm in M:
                found = True
                for i in range(len(D)):
                    d = D[i]
                    m = mm[i]
                    if get(x + d[0], y + d[1]) != m:
                        found = False
                        break
                if found:
                    t += 1
print("4b", t)

from collections import defaultdict

t = 0
u = False
o = defaultdict(list)
for l in open("5", "r").readlines():
    l = l.strip()
    if len(l) < 1:
        u = True
        continue
    if not u:
        a,b = l.split('|')
        o[int(b)].append(int(a))
    else:
        bad = False
        p = l.split(',')
        for i in range(len(p)):
            if bad:
                break
            for j in range(i+1,len(p)):
                if int(p[j]) in o[int(p[i])]:
                    bad = True
                    break
        if not bad:
            t += int(p[len(p)//2])

print("5a", t)

t = 0
u = False
o = defaultdict(list)
for l in open("5", "r").readlines():
    l = l.strip()
    if len(l) < 1:
        u = True
        continue
    if not u:
        a,b = l.split('|')
        o[int(b)].append(int(a))
    else:
        bad = False
        p = l.split(',')
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if int(p[j]) in o[int(p[i])]:
                    bad = True
                    p[j],p[i] = p[i],p[j]
        if bad:
            t += int(p[len(p)//2])

print("5b", t)
