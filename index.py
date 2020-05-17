import numpy as np
import functools
import math
import collections
import scipy
import fractions
import itertools

def solve():
  n, m = map(int, input().split())
  dokutu = [0]*m
  turo = [[] for i in range(n)]
  for i in range(m):
    dokutu[i] = list(map(int, input().split()))
    turo[dokutu[i][0]-1].append(dokutu[i][1])
    turo[dokutu[i][1]-1].append(dokutu[i][0])
  print(turo)
  for i in range(n):
    if len(turo[i]) == 0:
      print("No")
      exit()
  check = [-1]*n
  for i in range(n):
    for j in range(len(turo[i]))
  return 0
 
if __name__ == "__main__":
  solve()
