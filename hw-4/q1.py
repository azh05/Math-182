#!/usr/bin/python3

def brute_force(x, n): 
    product = 1
    for i in range(n):
        product = product * x

    return  product


def divide_and_conquer(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = divide_and_conquer(x, n // 2)
        return half_power * half_power
    else:
        half_power = divide_and_conquer(x, (n - 1) // 2)
        return x * half_power * half_power

def main():
    print(brute_force(2, 10))
    print(divide_and_conquer(2, 10))

if __name__ == '__main__':
    main()

