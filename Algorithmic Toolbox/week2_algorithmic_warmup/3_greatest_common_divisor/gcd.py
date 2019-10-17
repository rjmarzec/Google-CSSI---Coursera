# Uses python3
import sys

def euclid_gcd(a, b):
    current_gcd = 1

    if b == 0:
        return a
    else:
        current_gcd = euclid_gcd(b, a % b)

    return current_gcd

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(euclid_gcd(a, b))
