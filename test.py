print("Hello world!")

# Create variables
name = "Andrew"
last_name = "Reyna"
total = 12.99
age = 33
found = True

# if/else statement
if age < 100:
    print("don't worry you're not that old")
elif age == 100:
    print("Congrats you're a century")
else:
    print("sorry seems that your old!")

# Function
# function say_hello(){}
    
def say_hello():
    print("Hello there")
def say_goodbye(name):
    print("Goodbye"+ name)
# call a function
say_hello()
say_goodbye(" Andrew")

#concatenate
print("Hello my name is "+ name + " and I am "+ str(age)+" years old")

#array
#list -- the order matters
colorList = ["white","red","black","blue"]
numberList = [1,1,4,2,3]

#add
colorList.append("pink")

#travel the list
for colors in colorList:
    print(colors)

print(colorList[0])
 
#for(i=0;color.length;i++) -- travelling array in JS
    #let temp = color[i]
        #console.log(temp)

#dictionary -- the order of the elements does not matter as much as list
    
me={
    "first_name":"Andrew",
    "last_name":"Reyna",
    "age":37
}
print(me["first_name"])

me["age"] = 99 #modify the element "age"
me["color"] = "blue"
print(me)