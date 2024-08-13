#Find the runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(list(arr))
    
runner_up = sorted(arr_set)[len(arr_set) - 2]
print(runner_up)