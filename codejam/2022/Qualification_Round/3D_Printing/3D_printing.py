def three_d_printer(case: int):
    printer_1 = [int(i) for i in input().split(" ")]
    printer_2 = [int(i) for i in input().split(" ")]
    printer_3 = [int(i) for i in input().split(" ")]

    minimum_ink = [
        min(printer_1[0], printer_2[0], printer_3[0]),
        min(printer_1[1], printer_2[1], printer_3[1]),
        min(printer_1[2], printer_2[2], printer_3[2]),
        min(printer_1[3], printer_2[3], printer_3[3]),
    ]

    if sum(minimum_ink) < 1000000:
        minimum_ink = 'IMPOSSIBLE'

    else:
        while sum(minimum_ink) > 1000000:
            leftover = sum(minimum_ink) - 1000000
            max_of_min_index = minimum_ink.index(max(minimum_ink))
            if minimum_ink[max_of_min_index] > leftover:
                minimum_ink[max_of_min_index] -= leftover
            else:
                minimum_ink[max_of_min_index] = 0
        minimum_ink = ' '.join(str(i) for i in minimum_ink)

    print('Case #{}: {}'.format(case, minimum_ink))


for case in range(int(input())):
    three_d_printer(case + 1)
