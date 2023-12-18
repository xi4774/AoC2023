import os, sys, re

CURR_PATH = os.path.join(os.getcwd(), "D"+os.path.basename(__file__)[1:-3])

testEx = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

testEx2 = ''''''

def getlinesInput():
    file = open(os.path.join(CURR_PATH, 'input.txt'), 'r')
    return file.read().splitlines()

def getlinesExample(ex):
    return ex.splitlines()

def getTablesPart1(lines):
    nb_table = [[]] # Edge case 1st line
    symbol_table = [[]]
    for line in lines:
        # Get all start indexes + value of numbers for each line
        nb_table.append([(m.start(0), m.group(0)) for m in re.finditer("\d+", line)])
        symbol_idx = []
        for i, c in enumerate(line):
            if not(c.isdigit() or c=='.'):
                symbol_idx.append(i)
        symbol_table.append(symbol_idx)
    # Edge case last line
    nb_table.append([])
    symbol_table.append([])
    return nb_table, symbol_table

def part1(lines, debug=False):
    output = 0
    lenLine = len(lines[0])
    nb_table, symbol_table = getTablesPart1(lines)
    if debug:
        print(nb_table[:10], symbol_table[:10])
    # Go through each line
    for i, line in enumerate(nb_table[1:-1]):
        if len(line)>0:
            if debug:
                print(line)
                print(symbol_table[i], symbol_table[i+1], symbol_table[i+2])
            for nb in line:
                idx_start, val = nb[0], nb[1]
                idx_end = idx_start + len(val) - 1
                check_start, check_end = max(0, idx_start - 1), min(lenLine, idx_end + 1)
                skip = False
                for j in range(i, i+3): # Check line before, same and after
                    if not(skip) and len(symbol_table[j])>0:
                        for idx_symbol in symbol_table[j]:
                            if check_start <= idx_symbol <= check_end:
                                if debug:
                                    print(val)
                                output += int(val)
                                skip = True
                                break
        # if debug and i == 9:
        #     print(output)
        #     sys.exit()
    return output

def getTablesPart2(lines, debug=False):
    nb_table = [[]] # Edge case 1st line
    symbol_table = [[]]
    for line in lines:
        # Get all start indexes + value of numbers for each line
        nb_table.append([(m.start(0), m.group(0)) for m in re.finditer("\d+", line)])
        symbol_table.append([m.start(0) for m in re.finditer("\*", line)])
        # Edge case last line
    nb_table.append([])
    symbol_table.append([])
    return nb_table, symbol_table
    
def count_part_numbers(idx_gear, nb_neighbours, lenLine):
    cpt_part_numbers, gear_ratio = 0, 0
    for line_nb in nb_neighbours:
        if len(line_nb)>0:
            for nb in line_nb:
                idx_start, val = nb[0], nb[1]
                idx_end = idx_start + len(val) - 1
                check_start, check_end = max(0, idx_start - 1), min(lenLine, idx_end + 1)
                if check_start <= idx_gear <= check_end:
                    cpt_part_numbers += 1
                    if cpt_part_numbers == 1:
                        gear_ratio = int(val)
                    elif cpt_part_numbers == 2:
                        gear_ratio *= int(val)
                    else:
                        return -1, -1
    return cpt_part_numbers, gear_ratio
    
def part2(lines, debug=False):
    output = 0
    lenLine = len(lines[0])
    nb_table, symbol_table = getTablesPart2(lines)
    if debug:
        print(nb_table, symbol_table)
    for i, line in enumerate(symbol_table[1:-1]):
        if len(line)>0:
            for idx_gear in line:
                cpt_part_nb, gear_ratio = count_part_numbers(idx_gear, nb_table[i:i+3], lenLine)
                if cpt_part_nb == 2:
                    output += gear_ratio
    return output

if __name__ == "__main__":
    exLines = getlinesExample(testEx)
    # print(part1(exLines, True))
    inputLines = getlinesInput()
    # print(part1(inputLines))
    # 528819
    exLines2 = getlinesExample(testEx)
    print(part2(exLines2, True))
    print(part2(inputLines))
    # 80403602