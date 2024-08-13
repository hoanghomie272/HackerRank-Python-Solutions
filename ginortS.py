my_string = input()

lowercase = []
uppercase = []
odd_numbers = []
even_numbers = []

for char in my_string:
    if char.isdigit():
        if int(char) % 2 == 0:
            even_numbers.append(char)
        else:
            odd_numbers.append(char)
    elif char.isalpha():
        if char.islower():
            lowercase.append(char)
        else:
            uppercase.append(char)

sorted_list = sorted(lowercase) + sorted(uppercase) + sorted(odd_numbers) + sorted(even_numbers)

print(''.join(sorted_list))
