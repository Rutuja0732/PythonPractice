#6. Factorial Calculator
#Problem: Compute the factorial of a number using a while loop.
'''using for loop .......
number= int(input("enter a number  : "))
print("number is ",number)
factorial=0
for i in range(1,number):
    factorial = i* number
print(factorial)
'''
#using while loop 
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    factorial *= number
    number = number - 1

print("Factorial: ", factorial)