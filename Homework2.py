######Nare Sedrakyan#############

#Problem 1

import string

new_string = str(input('Enter a characters : '))

def is_all_uppercase(new_string):
    for c in new_string:
        if c not in string.ascii_uppercase:
            return False
    return True

new_string = str(input('Enter a characters : '))

if new_string = True:
    Print ("Yes")
else:
    Print ("No")



#Problem 2 
num = int(input("Input an integer:"))
def add_digits(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

print(add_digits(num)



#### Problem 3 


def largest_number(d, n): # d stands for digits
for i in range(n-1, 0, -1):
    if d[i] > d[i-1]:
    
      break
  
  if i == 0:
    
    print("No")
  
  x = d[i-1]
pos = i
for j in range(i+1, n):
    if d[j] > x and d[j] < d[pos]:
    pos = j
  
 d[i-1], d[pos] = d[pos], d[i-1] # Now, let's swapping the numbers at position j and i-1
  
 result = 0
for j in range(i):
    result = result * 10 + d[j]
  
    d = sorted(d[i:]) # sort all digits after i-1 in ascending order
  
  for j in range(n-i):
    result = result * 10 + digits[j]
    
    print("Yes")


Your_fav_number = int(input("Please enter a number:"))

d = map(int, Your_fav_number)
largest_number(d, len(Your_fav_number))
	
# Problem 4
def reverse(num): 
    Rev = 0
    while (num != 0): 
        rev = (Rev * 10) + (num % 10) 
        n //= 10
    return rev 
 
def getSum(num): # So we need to write a function in order to find the sum of the odd and even positioned digits in a number, 
                 #and then return true if both sums are = 
 
    n = reverse(num) 
    sumOdd = 0
    sumEven = 0
    k = 1
 
    while (num != 0): 
 
        if (k % 2 == 0): # If k is even number then, then digits extracted are at even places
            sumEven += num % 10
        else: 
            sumOdd += num % 10
        num //= 10
        k += 1
        
n = int(input("Please enter a number:"))
       
    if  sumEven == sumOdd: 
        print ("Yes") 
            
    else:
        print ("No") 
	
## Problem 6


def goldbach_s_conjecture ():
    num = int(input("Please, enter an even integer above 2: "))
    while num < 0 and num <= 2 or num % 2 != 0: 
        num = int(input("Please try again, the inputed number isn't even: ")) 
    return num

def Num_is_Prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
   
number = goldbach_s_conjecture()
print(number) 
prime = Num_is_Prime(number)
print(prime) 	
	
####	

