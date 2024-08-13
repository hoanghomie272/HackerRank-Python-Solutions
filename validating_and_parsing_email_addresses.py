import re
import email.utils

n = int(input())

s = [input().split() for _ in range(n)]

pattern = r'^[a-zA-Z][a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for my_list in s:
    name, email_addr = my_list[0], my_list[1].strip("<>")
    
    if re.match(pattern, email_addr):  
        print(email.utils.formataddr((name, email_addr)))
