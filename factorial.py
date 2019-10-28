def factorial(n):
## Your code - begin
  if n == 0: #this is the base case where the recursion logic terminates
    return 1
  else:
    return n * factorial(n - 1) #the is where the recursion takes place
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = factorial(n)
	print output
