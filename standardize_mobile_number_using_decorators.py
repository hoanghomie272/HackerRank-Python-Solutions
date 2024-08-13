def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for num in l:
            num = num[-10:]  
            formatted_numbers.append("+91 " + num[:5] + " " + num[5:])

        return f(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
