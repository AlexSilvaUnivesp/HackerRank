s = 'chris alan'

def solve(s):
    result = s[:1].upper()
    names = result + s[1:]
    for i in range(1, len(names)):
        if names[i-1] == ' ' and names[i] != ' ':
            result += names[i].upper()
        else:
            result += names[i]
    
    return result

print(solve(s))