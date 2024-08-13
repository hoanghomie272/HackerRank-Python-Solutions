cube = lambda x: x**3

def fibonacci(n):
    my_list = [0, 1]
   
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        for i in range(2, n):
            my_list.append(my_list[-1] + my_list[-2])

        return my_list
   

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))