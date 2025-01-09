#3. Multiplication Table Printer
#Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number= int(input("enter a number to calculate table of it : "))
print("number is ",number)
for i in range(1,11):
    if i==5:
        continue
    print(i*number)
