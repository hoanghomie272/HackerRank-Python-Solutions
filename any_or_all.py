N = int(input())
my_list = input().split()
if all(int(number) > 0 for number in my_list) and any(number[::-1] == number for number in my_list):
    print("True")
else: 
    print("False")