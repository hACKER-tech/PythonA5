# Array printing utility function. Feel free to use.
def printArr(arr, k): 
  for i in range(k): 
    print(str(arr[i]) + " "), 
  print
  
def printSeqUtil(n, k, len1, arr):  
## Your code - begin
  if  len1 == 0:
    i = 1
  elif len1 == k:
    return printArr(arr, k)
  else:
    i = arr[len1 - 1] + 1
  len1 = len1 + 1
  while (i <= n): 
    arr[len1 - 1] = i 
    printSeqUtil(n, k, len1, arr) 
    i = i + 1
  len1 = len1 - 1 
## Your code - end
  
def printSeq(n, k): 
    arr = [0] * k  
    len1 = 0
    printSeqUtil(n, k, len1, arr) 

if __name__ == "__main__":
  n = input("Enter n: ")
  k = input("Enter k: ")
  printSeq(n, k)
