import fractions as f

def evaluate(expr):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == '_':
            j = 1
            while expr[i + j] != '_' and expr[i + j] != '/' and expr[i + j] != '*' and expr[i + j] != '+':
                j += 1
            stack.append(variables[expr[i + 1:i + j]])
            i += j - 1
        else:
            b = stack.pop()
            a = stack.pop()
            if expr[i] == '/':
                stack.append(a/b)
            elif expr[i] == '*':
                stack.append(a*b)
            elif expr[i] == '+':
                stack.append(a+b)
        
        i += 1

    return stack.pop()


for i in range(1000):
    lines = []
    variables = {}

    case = input()
    while True:
        new_line = input()

        lines.append(new_line)

        right = new_line[new_line.find('=')+1:]
        right = right.split('/')

        if right[0].isdigit() and right[1].isdigit():
            break

    max_line = len(lines) - 1

    # fraction
    variables[lines[max_line][0:lines[max_line].find('=')]] = f.Fraction(lines[max_line][lines[max_line].find('=') + 1:])

    for j in range(max_line - 1, -1, -1):
        variables[lines[j][0:lines[j].find('=')]] = evaluate(lines[j][lines[j].find('=')+1:])

    results = sorted(variables.items(), key=lambda x: x[0])

    print("case " + str(i + 1) + " Y")
    for r in results:
        print(r[0], r[1].numerator, r[1].denominator)