user_value_1 = input("Enter the first value: ")

while type(user_value_1) != float:
    try:
        user_value_1 = float(user_value_1) 
    except ValueError:
        print("It was not a number!")
        user_value_1 = input("Enter the first value: ")

user_operator = input("Enter an operator: ")

if user_operator == "+" or user_operator == "-" or user_operator == "*" or user_operator == "/":
    user_value_2 = input("Enter the second value: ")
    while type(user_value_2) != float:
        try:
            user_value_2 = float(user_value_2)
        except ValueError:
            print("It was not a number!")
            user_value_2 = input("Enter the second value: ")
            while type(user_value_2) != float:
                try:
                    user_value_2 = float(user_value_2)
                except ValueError:
                    print("It was not a number!")
                    user_value_2 = input("Enter the second value: ")

elif type(user_operator) == float or type(user_operator) == str:
    print("It was not an operator!")
    user_operator = input("Enter an operator: ")
        
    if user_operator == "+" or user_operator == "-" or user_operator == "*" or user_operator == "/":
        user_value_2 = input("Enter the second value: ")
        while type(user_value_2) != float:
            try:
                user_value_2 = float(user_value_2)
            except ValueError:
                print("It was not a number!")
                user_value_2 = input("Enter the second value: ")
    elif type(user_operator) == float or type(user_operator) == str:
        print("Notice, operator is +, -, *, /. Choose one!")
        user_operator = input("Enter an operator: ")
        
        if user_operator == "+" or user_operator == "-" or user_operator == "*" or user_operator == "/":
            user_value_2 = input("Enter the second value: ")
            while type(user_value_2) != float:
                try:
                    user_value_2 = float(user_value_2)
                except ValueError:
                    print("It was not a number!")
                    user_value_2 = input("Enter the second value: ")

user_result = input("Enter an equal sign: ")
    
if user_result == "=" and user_operator == "+":
    result = user_value_1 + user_value_2
    print(result)
elif user_result == "=" and user_operator == "-":
    result = user_value_1 - user_value_2
    print(result)
elif user_result == "=" and user_operator == "*":
    result = user_value_1 * user_value_2
    print(result)
elif user_result == "=" and user_operator == "/":
    result = user_value_1 / user_value_2
    print(result)                
else:
    print("It was not an equal sign!")
    user_result = input("Enter an equal sign: ")