ejercicio solucion
def printPairs(arr, n, sum):
...
...     # count = 0
...
...     # Consider all possible
...     # pairs and check their sums
...     for i in range(0, n):
...         for j in range(i + 1, n):
...             if (arr[i] + arr[j] == sum):
...                 print("(", arr[i],
...                       ", ", arr[j],
...                       ")", sep="")
...
>>> # Driver Code
>>> arr = [1,9,5,0,20,-4,12,16,7]
>>> n = len(arr)
>>> sum = 12
>>> printPairs(arr, n, sum)
