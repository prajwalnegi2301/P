''' break statement execute hone ke baad nhi chlti loop bakki and continue ke implement hone ke baad bs vhi skip ho jaati hai bkki loop chlti hai '''

# break
for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("hi")

# continue
for i in range(7):
    
    
    if i==4:
        continue
    print(i)
    
   