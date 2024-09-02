# # wap to input user's first name & print its length

fn=input("enter 1st name: ")
print(len(fn))

# # wap to find occurence of '$' in a string

str="This is $ us currency which $ has $ values$ in india $value is high as $$$"
print("count of $ is ",str.count("$"))

# conditional statements
# if:elif:else
age=int(input("enter the age:"))
if(age>=18):
    print("Apply for license")
    print("can vote")
elif(age<=18):
    print("wait till you reach 18")
    print("Have patience")
else:
    print("Go watch pogo")

# WAP to check if a number entered by user is odd or even
a=int(input("enter the number:"))
if(a%2==0):
    print("even")
else:
    print("odd")


# WAP to find gretest of 3 numbers entered by user
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))

if(a>=b and a>=c):
    print(a, "a is greater")
elif(b>=c):
    print(b, "b is greater")
else:
    print(c, "c is greater")

#wap to check for multiple of 7 or not
a=int(input("enter a number :"))

if(a%7==0):
    print("yes the number ",a ,"is multiple of 7")
else:
    print("no ",a," it is not multiple of 7")