#Grupa Małek Paweł, Michalak Damian, Michalik Aleksander, Mączka Jakub
print("calculator")


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y



output = False
while output == False:

    print("::Menu::")
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - quit")

    choice = input("choose (1/2/3/4/5):")

    if choice == '6':
        question = input("Do you want to quit? (yes/no): ")
        if question == 'yes':
            output = True
            print('Bye!')
            exit()
        elif question == 'No':
            output = False
            print('You have backed to calculator')
            choice = input("choose (1/2/3/4/5):")

    x = float(input("give a number: "))
    y = float(input("give a number: "))

    if choice == '1':
        print(x, "+", y, "=", addition(x, y))

    elif choice == '2':
        print(x, "-", y, "=", subtraction(x, y))

    elif choice == '3':
        print(x, "*", y, "=", multiplication(x, y))

    elif choice == '4':
        print(x, "/", y, "=", division(x, y))

    else:
        print("This is not allowed")
        