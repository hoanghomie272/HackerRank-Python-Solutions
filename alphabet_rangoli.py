def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    list = []
    for i in range(size):
        elm = "-".join(alphabet[size - 1:i:-1] + alphabet[i:size])
        list.append(elm.center(4*size - 3, "-"))
    rangoli = "\n".join(list[::-1] + list[1:])
    print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
