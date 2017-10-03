#This is a program that displays all the prime numbers between a given range (10)
for num in range(2,10):
  if all(num%i!=0 for i in range(2, num)):
    print (num)