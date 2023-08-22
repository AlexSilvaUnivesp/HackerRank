s = "123"
alnum, alpha, digit, lower, upper = False, False, False, False, False
for i in range(len(s)):
    if s[i].isalnum(): alnum = True
    if s[i].isalpha(): alpha = True
    if s[i].isdigit(): digit = True
    if s[i].islower(): lower = True
    if s[i].isupper(): upper = True
    if alnum and alpha and digit and lower and upper: break
print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)