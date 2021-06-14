import sys
class Solution:
  def thirdLargest(self, arr, n):
    if(n < 3):
      return -1
    first = arr[0]
    second = -sys.maxsize
    third = -sys.maxsize
    for i in range(1, n):
      if(arr[i] > first):
        third = second
        second = first
        first = arr[i]
      elif(arr[i] > second):
        third = second
        second = arr[i]
      elif(arr[i] > third):
        third = arr[i]
    return third

t = int(input("Enter number of test cases:\n"))
for i in range(t):
  n = int(input("enter size of array:\n"))
  arr = list(map(int, input("enter your elements:\n").strip().split()))
  print(Solution().thirdLargest(arr, n))
