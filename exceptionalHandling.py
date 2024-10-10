''' try: and except: are use for to not to sop running code after error comes
try: is use where we think that error may come and except comes where alternative is provided like printing of some statement when error comes '''

a=input("enter value: ")
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)  
print("some imp lines of code")
print("end of code")    


a=input("enter value: ")
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print(" error has occured")  
print("some imp lines of code")
print("end of code")   

# valueError and indexError and many other types of error are there


# finally: statement will always get executed
try:
    l=[1,2,3,4,5,6]
    i=int(input("enter value: "))
    print(l[i])
except:
    print("some error occurred")    
finally:
    print("finally will always print even after error has detected by try-except statement whereas simple print statement will not work after error has come")

# some more examples
a=int(input("enter any value between 5 and 9"))
if(a<5 and a>9):
    raise ValueError("value should be between 5 and 9")






