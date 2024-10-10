# it allows us to iterate over a loop and get the index and value of each element in sequence at same time. 
fruits=["apple", "mango", "banana"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)



marks=[12,56,32,98,45,1,4]

index =0
for mark in marks:
    print (mark)
    if(index==3):
        print("harry, awesome!")
    index+=1    

