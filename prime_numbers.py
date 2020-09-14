def gen_prime(limit):
    primes = [] # Makes/clears the primes variable for later

    for num in range(2, limit + 1): # For every number that is from 2 to the limit(+ 1)
        if num > 1: # Makes sure it doesnt say 1 is a prime number

            for i in range(2, num): # Basically the same thing as before but this makes it check every number

                if (num % i ) == 0: # If the number can be divided it does nothing
                    break
                else: # If the number cant be divided it adds it into the primes variable
                    primes.append(num)
                    break
                
    return primes # Returns the prime numbers from the function back to where you called it from



if __name__ == "__main__": # This makes it for if you run the file directly
    output = gen_prime(int(input("Please enter your limit\n")))
    print("All the primes are:\n", output, "\nThere are", len(output), "numbers!")