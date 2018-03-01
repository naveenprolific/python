operators = {   '+' : 0,'-' : 0,'*' : 1,'/' : 1,'^' : 2, }

def infixtorpn(infixexp):
    rpnexp = ""
    opstack = []
    for i in range(0, (len(infixexp) - 1)):
        token = infixexp[i]
        # Operands
        if token >= 'a' and token <= 'z':
            rpnexp = rpnexp + token
            continue
        # Operators
        if token in operators:
            while len(opstack) > 0 and \
            opstack[-1] in operators and \
            operators[opstack[-1]] > operators[token]:
                rpnexp = rpnexp + opstack.pop()
            opstack.append(token)
            continue
        # Parenthesis
        if token == '(':
            opstack.append(token)
            continue
        if token == ')':
            while opstack[-1] != '(':
                rpnexp = rpnexp + opstack.pop()
            opstack.pop()
            continue
    # Pop remaining operators into output
    while len(opstack) > 0 and opstack[-1] != '(':
        rpnexp = rpnexp + opstack.pop()
    return rpnexp


# Number of test cases
testcases = input()
# Process each testcase
for testcase in range(0, testcases):
    print infixtorpn(raw_input())
