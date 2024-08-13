T = int(input())
div = []
for _ in range(T):
    div.append(input().split())
for i in range(T):    
    try:
        print(int(div[i][0]) // int(div[i][1]))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)