list1 = []
list2 = []

def LCM(num1, num2):
    i = 1
    
    while i < 1000:
        hold1 = num1 * i
        hold2 = num2 * i

        list1.append(hold1)
        list2.append(hold2)
        
        i += 1

    for num in list1:
        
        if num in list2:
            return num
            
        else:
            pass

if __name__ == "__main__":
    input1 = int(input("Enter the first number.\n"))
    input2 = int(input("Enter the second number.\n"))

    print("The LCM is:", LCM(input1, input2))

