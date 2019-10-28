def recurse(ans, n):
## Your code - begin
  if n < 2:
    return str(n) 
  else:
    return (recurse(ans, n/2) + str(n % 2))
## Your code - end

def decToBin(n):
  return recurse("", n) 

if __name__ == "__main__":
  n = input("Enter number: ")
  output = decToBin(n)
  print output
