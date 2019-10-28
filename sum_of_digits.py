def sumDigits(n):
## Your code - begin
  sum1 = 0
  if n != 0:
    a = sumDigits(n/10)
    return (n % 10 + a)
  else:
    return 0
## Your code - end

if __name__ == "__main__":
	n = input("Enter number: ")
	output = sumDigits(n)
	print output
