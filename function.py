# a=5
# b=10
# sum =a+b
# print(sum)

# #more lines of code 

# a=20
# b=10
# sum =a+b
# print(sum)

# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal_sum(5,10)
# cal_sum(10,20)

# function definition
# def cal_sum(a,b): #parameters
#     return a+b
# sum=cal_sum(1,4) #function call;arguments
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()


# average of 3 numbers 

# def cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return(avg)
# cal_avg(1,2,3)

# def cal_prod(a=1,b=4):
#     print(a*b)
#     return a*b

# cal_prod()

# def cal_prod(a, b=4):
#     print(a*b)
#     return a*b

# cal_prod(1)

# lets practice 
# Q.1= WAF to print the length of a list.(list is the prameter )

# cities = ["delhi" , "sakra" , "srinagar", "nielit","chennai"]
# heroes = ["thor","ironman", "captain", "shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# Q.2= WAF to printthe elements of a list in a single line.(list is the prameter)

# heroes = ["thor","ironman", "captain", "shaktiman"]
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(heroes)
# print()

# Q.3= WAF to find the factorial of n.(n is the parameter)

# n=5
# fact = 1
# for i in range(1, n+1):
#     fact *=i
# print(fact)

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i
#     print(fact)
# cal_fact(5)

# Q.4 = WAF to convert USD to INR 
# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val, "USD=",inr_val, "INR")

# converter(2)


# RECURSIVE FUNCTION 
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(9)

# def fact(n):
#    if(n==1 or n== 0):
#       return 1
#    return fact(n-1) * n
# print(fact(4))

# Lets Practice
# Q.1= Write a recursive function to calculate the sum of first n natural numbers.

# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1)+n
# sum = cal_sum(5)
# print(sum)


# Q.2 = Write a recursive function to print all elemets in a list. Hint : use list & indes as parameters.

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","lichi","apple","bannana"]
print_list(fruits)
