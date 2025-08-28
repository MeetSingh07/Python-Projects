# Making a Simple Calculator

# Functions - Addition , Subtraction , Multiplication , Division , Power

def addition(lst):
    print(f"Sum is {sum(lst)}\n")

def subtraction(num1 , num2):
    print(f"Subtraction is {num1-num2}\n")

def multiplication(lst):
    product=1
    for i in lst:
        product=product*i
    print(f"Product is {product}\n")

def division(num1 , num2):
    try:
        print(f"Division is {num1/num2}\n")
    except ZeroDivisionError:
        print("Error : Division by zero is not allowed\n")

def power(num , power1):
    print(f"{num} raise to the power {power1} is {num**power1}\n")

loop = "running"

while loop=="running":

    print(" " "Choose : \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n5 for Power \n6 to Exit" " ")
    choice = int(input("\nEnter your choice : "))

    if choice <1 or choice>6:
        print("Choose a valid choice.")
    
    elif choice==1:
        print("You chose Addition ( + )")
        n=int(input("How many numbers you want to add? : "))
        lst1=[]
        for i in range(1,n+1):
            lst1.append(int(input(f"Enter number {i} : ")))
        addition(lst1)
    
    elif choice==2:
        print("You chose Subtraction ( - )")
        n1=int(input("Enter 1st Number : "))
        n2=int(input("Enter 2nd Number : "))
        subtraction(n1 , n2)

    elif choice==3:
        print("You chose Multiplication ( * )")
        n1=int(input("How many numbers you want to multiply? : "))
        lst2=[]
        for i in range(1,n1+1):
            lst2.append(int(input(f"Enter number {i} : ")))
        multiplication(lst2)

    elif choice==4:
        print("You chose Division ( / )")
        number1=int(input("Enter number 1 : "))
        number2=int(input("Enter number 2 : "))
        division(number1,number2)

    elif choice==5:
        print("You chose Power ( ^ )")
        number=int(input("Enter the number : "))
        power1=int(input("Enter the power : "))
        power(number,power1)

    else:
        print("Exiting Calculator")
        loop="end"