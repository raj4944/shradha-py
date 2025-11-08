
name = input("Enter your Name: ")
print(name)
print("length of your name is:",len(name))
print("your name with first letter in capital is : ", str.capitalize(name))

#WAP to count a occurance of a character in your string
print("in the following string\nHi, i am your friend")
print("the letter 'i' appears for: ")
str = "Hi, i am your friend"
print(str.count("i"))

#conditional statement
print("if your age is greater than 18")
#nesting
age = 17
if(age >= 18):
    if(age >=80):
        print("can vote and apply for certificate")
    else: 
        print("you can not vote and can not apply for certificate if you are less than 18 years")