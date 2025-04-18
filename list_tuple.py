# marks =[94.4,87.5,99.9,66.4,78.8]
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ['ghufran',95.4,"Bihar"]
# print(student)

# note= string are immutable and list are mutable

# student = ['ghufran',95.4,"Bihar"]
# print(student[0])
# student[0] = "arjun"
# print(student)


# marks= [85,66,45,89]
# print(marks[1:4])
# print(marks[-3:-1])

# list = [2,1,5,0]
# list.append(4)
# print(list.sort(reverse=True))
# print(list)


# list = ['a','d','e','f','c','b']
# list.reverse()
# print(list)

# list = [2,1,3,4]
# # list.insert(1,5)
# # list.pop(2)
# list.remove(2)
# print(list)

# TUPLES IN PYTHON 
# LIST--MUTABLE
# STRING,TUPLE ---IMMUTABLE

# tup = (2,3,5,3)
# print(type(tup))
# print(tup[0])
# print(tup[1])

# tup = (1,)
# print(tup)
# print(type(tup))

# SLICING
# tup =(1,2,3,4,5)
# print(tup[1:3])
# tup =(1,2,3,4,5,4)
# print(tup.index(5))
# print(tup.count(4))


# PRACTICE QUESTION
# Q1= WAP TO ASK USER TO ENTER NAMES OF THEIR 3 FAVOURITE MOVIES & STORE THEM IN A LIST
# movies = []
# mov1 = input("enter 1st movie :")
# mov2 = input("enter 2nd movie :")
# mov3 = input("enter 3rd movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# movies = []
# mov = input("enter 1st movie :")
# movies.append(mov)
# mov = input("enter 2nd movie :")
# movies.append(mov)
# mov = input("enter 3rd movie :")
# movies.append(mov)
# print(movies)


# movies = []
# movies.append(input("enter 1st movie:"))
# movies.append(input("enter 2nd movie:"))
# movies.append(input("enter 3rd movie:"))
# print(movies)

# WAP TO CHECK IF A LIST CONTAINS PALINDRONE OF ELEMENT S.(HINT:USE COPY()METHOD)

# list1 = [1,2,1]
# list2 = [1,2,3]

list1 = ["m","a","a","m"]
copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

    