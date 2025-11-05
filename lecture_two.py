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
#str[4] ='@' change of character by their index is not allowed in python
ch = str[4]
print(ch)
print(str[7])
print(str[6])
#slicing part of the string, used in machine learning,accessing the part of the string.
str8 = "APNA IRISET"
print(str8[1:4])
print(str8[2:7])
print(str8[3:]) #this is accessing the string after 3rd index.
print(str8[3:len(str8)]) #this is also same as above, where it will read all indexes after 3 and print the full string
print(str8[:2])# this will print characters for index 0 and 1, that is MY

#slicing by negative index
print(str8[-3:]) #it will print SET from the string

#string function
str9 = "i am working in iriset"
print(str9.endswith("ing")) #this is false
print(str9.endswith("set")) #this is true

print(str9.capitalize())#capitalises the first letter of the string
print(str9.replace("iriset", "office of DG IRISET")) # it replaces the letter or work or a complete sentence in the strin
print(str9.find("o")) #it finds the 'o' in first available index
print(str9.count("o"))
print(str9.index("m"))
print(str9.index("i"), str9.count("i"))