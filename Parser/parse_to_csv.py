# This file will parse the accelerometer data from the Freedom K64 board to a csv file for use in generating visualizations


def canPush(S, state):
    if S == []:
        return False
    c = S[0]
    if state == 'empty': return alphaNum(c) or beginsSpecial(c)
    if state == 'id': return alphaNum(c)
    if state == 'num':
        # don't allow push if the following two chars are both '.'
        if len(S) > 1:
            if S[0] == '.' and S[1] == '.':
                return False
        return digit(c) or c == '.'
    if state == 'lessgreat': return c == '='
    if state == 'colon': return c == '='
    if state == 'period': return c == '.' or digit(c) or c == '('
    if state == "equal": return c == '>'
    if state == 'digitsAndPoint': return digit
