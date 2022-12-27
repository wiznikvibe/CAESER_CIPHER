# Program to check if a number is a prime number
def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("This is not a prime number.")
         

n = int(input("Check This Number: "))
prime_checker(number=n)
