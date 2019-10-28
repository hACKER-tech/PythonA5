def recurse(n, i):
## Your code - begin
  if i == (len(n) - 1)/2:
    return True
  else:
    if n[i] == n[len(n) - i - 1] and recurse(n, i + 1):
      return True
    else:
      return False
## Your code - end

def isPalindrome(n):
  return recurse(n, 0)
  
if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output
