import random

#slicing
h1=[1,2,3,4]
h2=h1[:]
print (h1)
print (h2)
h2=h1[1:3]
print(h2)
chai='masala chai'
print(chai)
slice_chai= chai[0:6]
print(slice_chai)
#gives the letter from right to left that is in reverse direction 
slice_chai=chai [-2]
print(slice_chai)

#imaginary numbers
a=2+1j
print (a)
b= a* 3
print(b)

#change of type

a= int (64)
print (a)
a= oct (64)
print (a)
a= hex (64)
print (a)

a= int ('64',8)
print (a)
a= int ('64',16)
print (a)

#import random package and get a random choice selected or as an output
l1=["Rutu","sam","geet","baby"]
print(l1)
print (random.choice(l1))
print (random.randint(5,25))
#shuffles the whole list
print(random.shuffle(l1))