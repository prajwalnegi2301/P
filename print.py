#printing list
list=[1,2,3,['h','t'],["hello","world"],2,3]
for i in list:
    print(i)
# replace command
practise="hello world"
print(practise.replace("hello","hi"))

# find command
practise="hello world"
print(practise.find("hello"))

# count command
practise="hello world"
print(practise.count("o"))

# printing ""
print("helllo my \"HFEH\"kghgh")
print('hefnj"hfue"sgh')

# separating using sep
print("dskjhf","kdsjhs",3243,3,sep=';')

# adding value to end
print("jhg", end=" 5gg")

# print using multi line
a='''hwegergr
grgergerg
gegergerger'''
print(a)

#printing upto limits
b="fwefewfew"
print(b[:3])

#capitalising every character
e="fsfsf"
print(e.upper())

#lowering every letter
c="fegeDFGD"
print(c.lower())

#capitaliszing first letter
d="fsdfg"
print(d.title())

# removing a particular character
f="##@@f@#dg@g@@"
print(f.rstrip("@"))

#creating comma between spaces
g="fwetwet fgeg greger"
print(g.split(" "))

#confirming that it ends with 
g="fslfjhoe"
print(g.endswith("hoe"))
print(g.endswith("e",0,1)) # same with startswith

#to know location of index
h="dskfb"
print(h.index("s"))
print(h.find("s"))

#isalpha returns true if all characters are alphabets
g="fewfw3"
print(g.isalpha())

#isalnum returns true is all characters are alphanumeric->a-z and 0-9 not->@##$$%1&*
j="rffd$%bt"
print(j.isalnum())

# to check title
g="Fsdg Fgf GDkmgd"
print(g.istitle())

# to capitalize and lower each character(reverse)
g="fsger JBJb JBIG KJNLjo"
print(g.swapcase())

#is printable() show false with \n and true with strings
#isspace() to check spsce is in between


# using range
for i in range(1,50,2):
    print(i)
















    
