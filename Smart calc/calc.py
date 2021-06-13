print("hello")
o= input ("input operation ")
x= int(input ("x = "))
y= int(input ("y = "))
if o == "+": 
    print (x+y)
elif o == "-":
    print (x-y)
elif o == "*" :
    print (x*y)
elif o == "/" : 
    if y==0 : 
        print ("it's a simple calc, don't be too smart")
    else :
        print (x/y)
elif o == "//" :
    if y==0 : 
        print ("it's a simple calc, don't be too smart")
    else :
        print (x//y)
elif o == "**" :
    print (x**y)
elif o == "%" :
    if y==0 : 
        print ("it's a simple calc, don't be too smart")
    else :
        print (x%y)
else :
    print ("Unknown operational symbol. It's a simple calc, don't forget" )
