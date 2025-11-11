movies = []
movie1 = input("Enter name of first movie: ")
#read = movie1
movie2 = input("Enter name of second movie: ")
#read = movie2
movie3 = input("Enter name of third movie: ")
#read = movie3
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)
#palindrome of an element
list1 = [2,4,7,4,2]
list2 = [2,5,7,9,7,5,2]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("palindrome")
else:
    print("Not palindrome")