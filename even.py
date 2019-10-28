def even_elements(l):
## Your code - begin
  a = []  
  a = [int(x) for x in range(len(l)) if x % 2 == 0]
  return a
## Your code - end
  
if __name__ == "__main__":
  l = range(10)
  print "input = ", l
  print even_elements(l)
