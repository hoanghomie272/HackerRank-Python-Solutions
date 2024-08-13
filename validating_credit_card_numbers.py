import re

def is_valid(number):
  
    if number[0] not in "456":
        return False

    if not re.fullmatch(r'[0-9-]+', number):
        return False
    
    if '-' in number:
        if len(number) != 19:
            return False
        lst = number.split('-')
        if len(lst) != 4:
            return False
        for chain in lst:
            if len(chain) != 4:
                return False
    else:
        if len(number) != 16:
            return False
    
    if re.search(r'(\d)\1{3}', ''.join(chars for chars in number.split('-'))):
        return False

    return True

T = int(input())
credit_card_numbers = [input().strip() for _ in range(T)]

for number in credit_card_numbers:
    if is_valid(number):
        print("Valid")
    else:
        print("Invalid")
