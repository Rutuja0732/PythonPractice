#2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number= int(input("enter a number to calculate sum of even numbers : "))
print(number)
sum=0
for num in range (1,number +1 ):
    if num % 2== 0:
       sum +=num
print("Sum of even numbers up to", number, "is:", sum)
 