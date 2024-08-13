import re

s = input()

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}+(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

consecutive_vowels = re.findall(pattern, s)

if consecutive_vowels == []:
    print("-1")
else:
    print('\n'.join(consecutive_vowels))