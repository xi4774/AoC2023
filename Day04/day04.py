import os, sys, re

CURR_PATH = os.path.join(os.getcwd(), "D"+os.path.basename(__file__)[1:-3])

testEx = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

testEx2 = ''''''

def getlinesInput():
    file = open(os.path.join(CURR_PATH, 'input.txt'), 'r')
    return file.read().splitlines()

def getlinesExample(ex):
    return ex.splitlines()

def part1(lines, debug=False):
    output=0
    for line in lines:
        _, numbers = line.split(": ")
        winningNb, drawNb = numbers.split(" | ")
        winningNb = winningNb.split()
        drawNb = drawNb.split()
        if debug:
            print(winningNb)
        cpt=-1
        for nb in drawNb:
            if nb in winningNb:
                if debug:
                    print(nb)
                cpt += 1
        if cpt>=0:
            points = 2**cpt
            if debug:
                print(points)
            output += points
    return output
    
    
def part2(lines, debug=False):
    lstWinNb = []
    for line in lines:
        _, numbers = line.split(": ")
        winningNb, drawNb = numbers.split(" | ")
        winningNb = winningNb.split()
        drawNb = drawNb.split()
        if debug:
            print(winningNb)
        cpt=0
        for nb in drawNb:
            if nb in winningNb:
                if debug:
                    print(nb)
                cpt += 1
        lstWinNb.append(cpt)
    if debug:
        print(lstWinNb)
    lstScratchedTimes = [1] * len(lstWinNb)
    for i, card in enumerate(lstWinNb):
        toScratchNb = lstScratchedTimes[i]
        for j in range(i + 1, i + card + 1):
            if j<=len(lstScratchedTimes):
                lstScratchedTimes[j] += toScratchNb
    if debug:
        print(lstScratchedTimes)
    return sum(lstScratchedTimes)

if __name__ == "__main__":
    exLines = getlinesExample(testEx)
    print(part1(exLines, True))
    inputLines = getlinesInput()
    print(part1(inputLines))
    exLines2 = getlinesExample(testEx)
    print(part2(exLines2, True))
    print(part2(inputLines))