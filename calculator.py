first_number=input("enter first number " )
operator=input("enter operator " )
second_number=input("enter second number " )
first_number=int(first_number)
second_number=int(second_number)
if operator =='+':
    print(first_number+second_number)
elif operator =='-':
    print(first_number-second_number)
elif operator =='*':
    print(first_number*second_number) 
elif operator =='/':
    print(first_number/second_number)    
elif operator =='%':
    print(first_number%second_number) 
else :
    print("not defined")         


