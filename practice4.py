#to check if the number is even or odd.
num = int(input("Enter your number: "))
#rem = num % 2
if(num % 2 == 0):
    print("even")
else:
    print("odd")
#to find the greatest of 3 numbers entered by user
a = int(input("Enter your first number: "))
b = int(input("enter your Second number:"))
c = int(input("Enter your Thirsd umber: "))
if(a >= b and a >= c):
    print("First number is larger", a)
elif(b >= c):
    print("Second number is largest", b)
else:
    print("Third number is largest", c)
#check if a number is a multiple of 7 or not
print("In the below example lets try to find if a number is multiple of 7 or not")
x = int(input("Enter the number"))
if (x % 7 == 0):
   print("It is multiple of 7")
   print("Thank you for trying")
else:
    print("this number is not the multiple of 7")
    print("Thank you for trying")

