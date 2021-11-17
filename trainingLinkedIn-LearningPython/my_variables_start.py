#
# My firt Python script
#

#Declare a variable and initialize it
f=0
print(f)
f="abcde"
print("f= " + f)

print("this is a string ")
print ("this is a string " + "abc")
print("this is a string " + str(123))
print("this is a string" , "abc")
print("this is a string" , f)
print ("this is a string " + f)

def someFunction():
    global f
    f="del"
    print(f)

someFunction()
print(f)
