def detect_floating_point_number(my_string):
    if my_string == "0":
        return False 
    try:
        float(my_string)
        return True
    except ValueError:
        return False

T = int(input())
my_list = [input() for _ in range(T)]
for my_string in my_list:
    if detect_floating_point_number(my_string):
        print("True")
    else:
        print("False")