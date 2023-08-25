def minion_game(string):
    vowels = 'AEIOU'
    score_kevin, score_stuart = 0, 0
    for l in range(len(s)):
        if s[l] in vowels:
            score_kevin += (len(s) - l)
        else:
            score_stuart += (len(s) - l)
    
    if score_kevin > score_stuart:
        print('Kevin', score_kevin)
    elif score_stuart > score_kevin:
        print('Stuart', score_stuart)
    else:
        print('Draw')


s = 'ANANAS'
minion_game(s)