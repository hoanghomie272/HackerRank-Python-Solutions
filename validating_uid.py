import re

def is_valid_uid(uid):
    if len(uid) != 10 or not uid.isalnum():
        return False
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    if len(re.findall(r'[0-9]', uid)) < 3:
        return False
    
    if len(set(uid)) != len(uid):
        return False
    
    return True

T = int(input())
uids = [input() for _ in range(T)]

for uid in uids:
    if is_valid_uid(uid):
        print("Valid")
    else:
        print("Invalid")