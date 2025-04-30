# 1: Write a function that takes in a person's name, and prints out a greeting.

# list of friends.
friends = ["John", "Michael", "Oliver"]
# list of greetings
greetings = ["hello [friend], how are you doing.", "Hows the weather treating you [friend].", "How ya been [friend]."]

# goes through greetings
for x in greetings:
    # goes through friends
    for y in friends:
       #replaces [friend] with friends (y)
        final = x.replace("[friend]", y)
        print(final)


# 2: Full name function

#function that accepts two objects
def full_name(x,y):
    #Formats result by stripping white space on either end and creates greeting
    print("Hello, " + str.strip(x) + " " + str.strip(y))

full_name("Daniel", "Tafmizi")
full_name("   Doctor ", "   Friedman")
full_name("Abraham", "Lincoln")

#3 addition calculator

#function with two objects
def add(x,y):
    #creats string version for print
    px = str(x)
    py = str(y)
    #creates string of sum of the objects
    z = str(x + y)
    #prints the objects
    print("Howdy, the sum of " + px + " and " + py + " is " + z)

add(7, 12)
add(29, 100)
add(43, 1)

#was curious for how to include any number of arguments. *args
def add_everything(*args):
    print(sum(args))

add_everything(2,2,2,2,2,2,2,2,2,2,2,2)

#4 return calculator

# wanted to try for loop to add many objects
#Initially used *args but had trouble with iteration. Decided to insert a list and return a list
def add_everythingR(int_list:list):
    #creates new list to fill
    string_list = []
    #r1 sums the given list and converts to string and appends to new list
    r1 = string_list.append (str((sum(int_list))))
    #r2 iterates over given list to convert ints to strings and appends to new list
    for int in int_list:
        r2 = string_list.append(str(int))
    return(string_list)


nums = [7,24,13,6]

result = add_everythingR(nums)

#Chatgpt code for formatting, removes quotes and brackets.
formatted_numbers = ', '.join(map(str, result[1:]))
formatted_sum = result[0]

print("The sum of the integers {} equals {}".format(formatted_numbers,formatted_sum))

#5 debug pow

print(pow(16,(1/2)))
# The code is giving the correct answer? 4
# Pow accepts three args; base, exp, and modulus
help(pow)

#6

#list list tuple
x=[1, 2, 3, 4, 5]
y=[11, 12, 13, 14, 15]
z=(21, 22, 23, 24, 25)

#a 3*x
print(3 * x)
# It reiterates the list three times

#b x+y
print(x+y)
# It joins the two lists together

#c x-y
#print(x-y)
#this is not a supported operand for lists, TypeError

#d x[1]
#value = 2

#e x[0]
#value = 1

#f x[-1]
#value = 5

#g x[:]
print(x[:])
#value = [1,2,3,4,5]

#h x[2:4]
#value = [3,4]

#i x[1:4:2]
print(x[1:4:2])
#value = [2, 4] Third variable is a "step", includes every second element from start to stop

# j x[:2]
print(x[:2])
# value = [1, 2]

# k x[::2]
print(x[::2])
#value = [1, 3, 5], only steps

#l x[3]=8
x[3]=8
#replaces the third list object with 8
print(x)

#(m) What is the result of the above pair of expressions if the list x were
#replaced with the tuple z?
# z[3]=8
print(z)
#TypeError: 'tuple' object does not support item assignment, tuples are immutable

