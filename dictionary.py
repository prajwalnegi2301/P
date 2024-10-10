'''1. dictionaries are ordered
2. .get(' fjsjhf') function will not give error, it will show none
3. keys come first then after ':', values comes '''

dic={"name":"harry", "age":19, "occupation":"coder"}
print(dic["name"])

# .get()
print(dic.get("car"))

# keys and values
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])

for key, value in dic.items():
    print(f"the value corresponding to key {key} is {value}")    

# update func is same as in sets
# clear func is also same
# e={} will create empty dictionary

# pop func is also same
#dic.popitem()
#print(dic)

# del dic and then print will give error as in sets
# del(dic["name"]) is also same, this can show error as string nahi hai




