sum = 0
while (True):
    userInput = input("Enter the number\nor press q to quit\n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Order total is so far:{sum}")

    else:
        print(f"The total bill if {sum}") 
        print("Thanks for Connecting With Us")   
        break

