def merge_the_tools(string, k):
    n = len(string)
    lst = [string[i*k:(i + 1)*k] for i in range(n // k)]
    
    for elm in lst:
        seen = []
        result = []
        for letter in elm:
            if letter not in seen:
                seen.append(letter)
                result.append(letter)
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)