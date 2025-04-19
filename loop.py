# count = 1
# while count <= 5:
#     print("hello")
# #     count +=1
# # print(count)

# i=1
# while i <= 5:
#     print("ghufran")
#     i+=1

# print numbers from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1
# print("loop ended")


# i=5
# while i>=1:
#     print(i)
#     i-=1
# print("loop ended")

# print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# print numbers from 100 to 1.
# i=100
# while i>=1:
#     print(i)
#     i-=1

# print the multiplication table of a number n.
# n = int(input("enter number :"))
# i=1
# while i<=10:
#     print(n*i)
#     i += 1


# print the element of the following list using a loop:
# [1,4,9,25,36,49,64,81,100]
# nums = [1,2,4,9,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# search for a number x in this tuple using loop:
#(1,4,9,25,36,49,64,81,100)

# nums = (1,4,9,25,36,49,64,81,100)

# x= 36
# i = 0
# while i < len(nums):
#     if(nums[i]== x):
#        print("found at idx",i)
#     else:
#         print("finding...")
#     i +=1


# BREAK & CONTINUE
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("end of loop")

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1


# ODD NUMBER 
# i=0
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# EVEN NUMBER 
# i=0
# while i<=5:
#     if(i%2 !=0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)

# str = "md ghufran alam"
# for char in str:
#     if(char == 'a'):
#         print("a found")
#         break
#     print(char)
# else:
#     print("END")

# LETS PRACTICE QUESTION

# print the elements of the following list using a loop:
# [1,4,16,25,36,49,64,81,100]
# nums = [1,4,16,25,36,49,64,81,100]
# for el in nums :
#     print (el)

# search for number x in this tuple using loop
# (1,4,16,25,36,49,64,81,100)

# nums = (1,4,16,25,36,49,64,81,100,49)
# x=49
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx",idx)
#         break
#     idx +=1


# RANGE
# seq = range(15)
# for i in seq:
#     print(i)

# for i in range(10): range(stop)
#     print(i)

# for i in range(2,10): range(start,stop)
#     print(i)

# for i in range(1,100,2): #range(start ,stop, step)
#     print(i)

# lets practice  using for & range()

# q1= print numbers from 1 to 100.
# for i in range(1,101):
#     print(i)

# q2 = print numbers from 100 to 1.
# for i in range (100,0,-1):
#     print(i)

# q3 = print the multiplication table of a number n.
# n = int(input("enter number :"))

# for i in range(1,11):
#     print(n*i)

#  PASS STATEMENT = pass is a null statement that does nothing .it is used as a placeholder for future code.

# for i in range (5):
#     pass
# print("some useful work")

#lets's practice 
# q1= wap to find the sum of first n natural  numbers .(using while)

# n= 7
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum=",sum)

# n= 7
# sum = 0
# i=1

# while i <= n:
#     sum += i
#     i +=1

# print("total sum=",sum)


# wap to find the factorial of first n numbers .(using for)


# n= 5
# fact = 1
# i=1

# while i <= n:
#     fact *= i
#     i +=1

# print("factorial =",fact)

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial =", fact)