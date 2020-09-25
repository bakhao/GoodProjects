import cv2
import django as dj

from sklearn import datasets
from itertools import permutations

print(dj.get_version())
cap = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
hello = "Hello guys"
print("Hello guys")


# (0,0) (0,1) (1,0) (1,1)


class Solution(object):
    def canThreePartsEqualSum(self, A):
        isinstance(A, list)
    pass




class Solution(object):
    def isBoomerang(self, points):
        count = True
        for i in range(len(points)):
            for j in range(len(points[i])):
                print('points[0][i]', points[i][1])
                if points[0][1] != points[1][1]:
                    count = True
                else:
                    count = False
        return count


def nth_smallest(arr, pos):
    arr = list(arr)
    arr = sorted(arr)
    print(arr)
    return arr[pos-1]

def group_by_commas(n):
    n = str(n)
    n = list(n)
    liste = []
    for i in reversed(range(len(n))):
        print(i)
        liste.append(n[i])
    return liste

print(group_by_commas("10000"))
