str="methodoverlaoding"
print(str)
print(len(str))
print(str[4]) #fetching a character at a given Index

#str[3]="e" this is wrong we cannot initialize a value in string

# slicing- fetching substring
str="college"
#    0123456
print(str[2:6])  #output- lleg
print(str[2:])  #output- llege

# a p p l e
#-5-4-3-2-1
str="apple"
print(str[-3:-1])


# String functions
str="karnataka"
print(str.find("a"))
print(str.count("a"))