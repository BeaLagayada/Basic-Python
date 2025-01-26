while True:
    n = int(input("\nEnter an integer n >= 2: "))
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        break
    else:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                print(f"The smallest factor other than 1 for {n} is: {i}")
                break

        if is_prime:
            print(f"{n} is a prime number.")




