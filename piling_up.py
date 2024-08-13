def can_stack_cubes(cubes):
    left, right = 0, len(cubes) - 1
    last_picked = float('inf')  
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            pick = cubes[left]
            left += 1
        else:
            pick = cubes[right]
            right -= 1
        
        if pick > last_picked:
            print("No")
            return
        
        last_picked = pick
    
    print("Yes")


T = int(input())
for _ in range(T):
   
    n = int(input())
    cubes = list(map(int, input().split()))
    can_stack_cubes(cubes)
