def recurse(n, i):
## Your code - begin

    k=len(n)
    #base case
    #recursion ends when the index reaches middle of the string  
    if (i==(k-1)/2 or i==(k/2)):
        return True

    #compare first element and last element of the string 
    #if matched recurse over same string 
    #now compare second element and second last element and so on  
    #if not matched in any recursion :return false
    elif(n[i]!=n[len(n)-i-1]):
        return False
    else:
        return recurse(n,i+1)

## Your code - end

def isPalindrome(n):
  return recurse(n, 0)
  
if __name__ == '__main__':
	n = raw_input("Enter string: ")
	output = isPalindrome(n)
	print output
