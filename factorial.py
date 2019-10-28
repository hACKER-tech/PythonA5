def factorial(n):
## Your code - begin
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = factorial(n)
	print output
