def print_formatted(number):
    max_width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(f"{i:>{max_width}} {oct(i)[2:]:>{max_width}} {hex(i)[2:].upper():>{max_width}} {bin(i)[2:]:>{max_width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)