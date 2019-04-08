##fileptr=open("python.txt","r")
##a=fileptr.read()
##print(a)
##fileptr.close()
##
##file1ptr=open("python.txt","r")
##print("File pointer is at byte :",file1ptr.tell())
####content=file1ptr.read()
##file1ptr.seek(60)
##print("After reading File pointer is at byte :",file1ptr.tell())
##
##import os;
##os.rename("python.txt","PYTHON.txt")
##if os.rename:
##    print("OK")
##else:
##    print("NOT OK")
##os.remove("PYTHON.txt")
##          

##import mod
##name=input("Enter your Name :")
##mod.displaymsg(name)


from mod import summation
##print("SUMMATION")
##a=int(input("Enter a number :"))
##b=int(input("Enter another number :"))
##print("Sum = ",summation(a,b))
##
##from mod import multiply
####print("MULTIPLICATION")
##a=int(input("Enter a number :"))
##b=int(input("Enter another number :"))
##print("Multiply =",multiply(a,b))
##
##
##from mod import divide
####print("DIVIDE")
##a=int(input("Enter a number :"))
##b=int(input("Enter another number :"))
##print("DIVIDE =",divide(a,b))


import json
list= dir(json)
print(list)



















