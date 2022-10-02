"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    n = 2
    if number_of_primes <= 0:
        raise ValueError(f'Number of primes={number_of_primes} needs to be at least 1.')
    elif number_of_primes == 1:
        list.extend([n])
    else:
        list.extend([n])
        n = n + 1
        counter = 0
        while len(list) < number_of_primes:
            counter = 0
            for i in range(len(list)):
                if n%list[i]!=0:
                    counter = counter + 1
            if counter == len(list):
                list.extend([n])
                n = n + 2
            else:
                n = n + 2

    return list
