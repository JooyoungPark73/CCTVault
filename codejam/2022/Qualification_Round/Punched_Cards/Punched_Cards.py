def punchCard(case):
    inputval = input().split(' ')
    row = int(inputval[0])
    column = int(inputval[1])
    print('Case #{}: '.format(case))
    first_top = str('..') + str('+-') * (column - 1) + str('+')
    first_bot = str('..') + str('|.') * (column - 1) + str('|')
    general_top = str('+-') * column + str('+')
    general_bot = str('|.') * column + str('|')
    last = str('+-') * column + str('+')

    print(first_top)
    print(first_bot)
    for r in range(row - 1):
        print(general_top)
        print(general_bot)
    print(last)


for case in range(int(input())):
    punchCard(case + 1)