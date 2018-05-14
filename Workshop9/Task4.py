def matchesTop(stack, endBracket):
    topBracket = stack.pop()
    stack.append(topBracket)
    if topBracket == '(':
        return endBracket == ')'

    elif topBracket == '[':
        return endBracket == ']'
    
    elif topBracket == '{':
        return endBracket == '}'

    else:
        return False

def checkBrackets(brackets):
    stkBrackets= []
    for bracket in brackets:
        
        if bracket in '({[':
            stkBrackets.append(bracket)
            
        elif (bracket in ')}]') and (matchesTop(stkBrackets, bracket)):
            stkBrackets.pop()
            
        else:
            return False
        
    if len(stkBrackets) == 0:
        return True
    return False


brackets = input('give a string of brackets: ')
if checkBrackets(brackets):
    print('YES')
else:
    print('NO')