import os
import re

def solve(s):
    result = re.sub(r'\b\w', lambda match: match.group().upper(), s)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()