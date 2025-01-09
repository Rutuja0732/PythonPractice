#4. Reverse a String
#Problem: Reverse a string using a loop.

str1 = str(input("enter a string to reverse it  : "))
print("string is : ",str1)

reversed_str=" "

for char in str1:
    reversed_str = char + reversed_str 
print("reversed string is : ",reversed_str)