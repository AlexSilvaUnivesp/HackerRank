def get_letters(start, end):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rangoli = ''
    for i in range(start -1, end, -1):
        rangoli += alphabet[i]
    for i in range(end, start):
        rangoli += alphabet[i]
    return '-'.join(rangoli)

def print_rangoli(size):
    width = size * 4 - 3
    for i in range(size-1, 0, -1):
        pattern = get_letters(size, i)
        print(pattern.center(width, '-'))
    for i in range(0, size):
        pattern = get_letters(size, i)
        print(pattern.center(width, '-'))

print_rangoli(26)
