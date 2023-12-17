## Day 1 AoC 2023

import re, os, sys

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }

CURR_PATH = os.path.join(os.getcwd(), "D"+os.path.basename(__file__)[1:-3])
print(CURR_PATH)
testEx = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

testEx2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

# lines = testEx.splitlines()

def getlinesInput():
    file = open(os.path.join(CURR_PATH, 'input.txt'), 'r')
    return file.readlines()

def getlinesExample(ex):
    return ex.splitlines()

def part1(lines, debug=False):
    output = 0
    
    for line in lines:
        line = re.sub('\D', '', line)
        if debug:
            print(f"{line[0]}{line[-1]}")
        output += int(f"{line[0]}{line[-1]}")
    return output

def findFirst(digit, line):
    try:
        return line.index(digit), digit
    except ValueError:
            return len(line), None
        
def findLast(digit, line):
    return line.rfind(digit), digit

def part2(lines, debug=False):
    output = 0
    for line in lines:
        res = ""
        idxFirstDigit = re.search(r"\d", line)
        idxmin, rep_digmin = min(findFirst(digit, line) for digit in digits)
        if idxFirstDigit:
            if idxFirstDigit.start() < idxmin:
                res += line[idxFirstDigit.start()]
            else:
                res += digits.get(rep_digmin)
        else:
            res += digits.get(rep_digmin)
        idxLastDigit = re.search(r"\d", line[::-1])
        idxmax, rep_digmax = max(findLast(digit, line) for digit in digits)
        if idxLastDigit:
            idxLastDigit = len(line) - idxLastDigit.start() - 1
            if idxLastDigit > idxmax:
                res += line[idxLastDigit]
            else:
                res += digits.get(rep_digmax)
        else:
            res += digits.get(rep_digmax)
        if debug:
            print(line[:-1] + "   " + res)
        output += int(res)
    return output

if __name__ == "__main__":
    # exLines = getlinesExample(testEx)
    # print(part1(exLines, True))
    inputLines = getlinesInput()
    print(part1(inputLines))
    exLines2 = getlinesExample(testEx2)
    # print(part2(exLines2, True))
    print(part2(inputLines))
    # 56324
