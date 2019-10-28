def double(l):
## Your code - begin
  for i in range (len(l)):
    l[i] = 2*l[i]
  double = l
  return double
## Your code - end
if __name__ == "__main__":
  l = [1, 2, 3]
  print "input = ", l
  print double([1, 2, 3])
