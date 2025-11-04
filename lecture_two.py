str1 = "This is a srting with double quote"
str2 = 'This is aother style of string with single quote'
str3 = """this is string with multiple line comment
this line is also in triple quote
"""
print(str1)
print(str2)
print(str3)
# this string like using user's will create error because python will read half the string upto user' and 's will not be read.
str4 = "this is another example where we can print two lines with single string.\nthe print will be like this after running the code"
#use \n before the start of second line.
#now print the string and observe the output
print(str4)
#we can use \t to continue in the same line with tab.
str5 = "same as above.\twill be printed in the second line"
print(str5)

#adding two string is called as concatenation
str6 = "MY\t"
str7 = "IRISET"
final_str = str6 + " " + str7
print(final_str)
len1 = len(str6)
len2 = len(final_str)
print(len1)
print(len2)

#indexing is a position of character in the string
#like   IRISET
# index 012345
#to print the character based on index number
str = "MY IRISET"
#str[4] ='@'
ch = str[4]
print(ch)
print(str[7])
print(str[6])
#slicing part of the string
str = "APNA IRISET"
str1 = str 
str2[1:4]
str1[2:7]
print(str1)
print(str2)