x=4
# x is variable to match
match x:
    case 0:
        print("zero")
    case 4:
        print("four")
    case _:
        print(x)       