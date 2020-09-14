def factor(num):
    output = []

    for i in range(1,num+1):
        
        if num%i==0:
            output.append(i)
        
    return output    


if __name__ == "__main__":
    number = int(input("Please enter a number.\n"))
    
    numbers = factor(number)

    print("The factors are:", numbers, "\n It has", len(numbers), "numbers ")