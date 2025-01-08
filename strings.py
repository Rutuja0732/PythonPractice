#slicing
print ("This is slicing")
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

print("***-------Methods that can be performed on string-------------***")

text="I am learning Python"
print("original string")
print(text)

#lower(): Converts all uppercase characters in a string into lowercase
print("\nConverted String to lowercase:")
print(text.lower())

#upper(): Converts all lowercase characters in a string into uppercase
print("\nConverted String to uppercase:")
print(text.upper())

#title(): Convert string to title case
print("\nConverted String to titlecase:")
print(text.title())

#swapcase(): Swap the cases of all characters in a string
print("\nConverted String to swapcase:")
print(text.swapcase())

#capitalize(): Convert the first character of a string to uppercase
print("\nConverted String as capitalize:")
print(text.capitalize())

#strip:- removes spaces before and after the string
chai= "    masala chai  "
print (chai)
print(chai.strip())

#replace
tea= "lemon tea"
print(tea)
print(tea.replace("lemon","ginger")) 

#find-gives the index position from where we can get the string described. if not found returns -1
print(tea.find("tea"))
print(tea.find("chai"))

#counting number of times element appears
tea1="masala tea, lemon tea, ginger tea, black tea "
print(tea1.count("e"))
print(tea1.count("tea"))

# format method with placeholders{}
tea2="masala chai"
quantity="2"
order="i want to order {} cups of {} "
print(order.format(quantity, tea2))

#join method -used to convert list to string form
tea3=["masala", "lemon" ,"ginger" ,"black "] 
print(" ".join(tea3))

#len
print(len(tea3))
# print each element in loop 
for i in tea:
    print(i)
#printing with multiple other techniques
let= "when we want to use  :\": in sentence we can write it as  \"I am rutuja\" like this "
print (let)

let1="if want to have addition of slashes etc while giving any path use \n r as raw string"
print(let1)
let2=r"if want to have addition of slashes etc while giving any path use \n r as raw string"
print(let2)
