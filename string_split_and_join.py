def split_and_join(line):
    string = "-".join(line.split())
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)