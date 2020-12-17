n = input("Enter the first value: ")

while type(n) != float:
    try:
        n = float(n) 
    except ValueError:
        print("It was not a number!")
        n = input("Enter the first value: ")

m = input("Enter an operator: ")
if m == "+" or m == "-" or m == "*" or m == "/":
    a = input("Enter the second value: ")
    
    while type(a) != float:
        try:
            a = float(a)
        except ValueError:
            print("It was not a number!")
            a = input("Enter the second value: ")
    
    b = input("Enter an equal sign: ")
    
    if b == "=" and m == "+":
        result = n + a
        print(result)
    elif b == "=" and m == "-":
        result = n - a
        print(result)
    elif b == "=" and m == "*":
        result = n * a
        print(result)
    elif b == "=" and m == "/":
        result = n / a
        print(result)                
    else:
        print("It was not an equal sign!")
        b = input("Enter an equal sign: ")

else:
    print("It was not an operator!")
    m = input("Enter an operator: ")