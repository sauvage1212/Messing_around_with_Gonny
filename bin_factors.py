def bin_factors(numb: int) -> list[any]:
    if numb < 2:
        raise ArithmeticError("Cannot work out prime factors of: " + str(numb))
    prime_factors = []
    primes = [2]
    i = 2
    working_numb = numb
    while True:
        primes = [2]
        j = True
        # print("Bucko, ", int(working_numb ** 0.5), ", ", working_numb, ", ", i)
        for k in range(int(working_numb ** 0.5)):
            if working_numb % i == 0 and j == True:
                prime_factors.append(i)
                working_numb = int(working_numb / i)
                j = False
                i = 2
                if working_numb == 1:
                    return prime_factors
                
            else:
                if j == True:
                    # print("Working out prime after ", i)
                    next_prime = i + 1
                    sub_loop = True
                    while sub_loop:
                        not_prime = False
                        for h in primes:
                            if next_prime % h == 0:
                                not_prime = True
                        if not not_prime:
                            i = next_prime
                            primes.append(next_prime)
                            sub_loop = False
                        else:
                            next_prime += 1
                        
                            

# plan:
# Keep inding any pair factors until numb is prime
# divide numb by 2 and if result whole return 2 and result else try with 3

def test():
    print("The prime factors of 1 are: ", bin_factors(1))
    # print(bin_factors(10))
    # print(bin_factors(1))
    # print(bin_factors(0))
    # print(bin_factors(84))
    # print(bin_factors(-84))

def ask():
    print(bin_factors(int(input("What do you want the prime factors of?"))))

ask()