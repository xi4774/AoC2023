import os, sys

CURR_PATH = os.path.join(os.getcwd(), "D"+os.path.basename(__file__)[1:-3])

testEx = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

testEx2 = ''''''

max_balls = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def getlinesInput():
    file = open(os.path.join(CURR_PATH, 'input.txt'), 'r')
    return file.readlines()

def getlinesExample(ex):
    return ex.splitlines()

def isPossibleGame(games):
    for game in games:
        colors = game.split(", ")
        for color in colors:
            val, col = color.split()
            if int(val) > max_balls.get(col):
                return False
    return True

def part1(lines, debug=False):
    output = 0
    for line in lines:
        game_id, games = line.split(":")
        _, game_id = game_id.split(" ")
        games = games.split("; ")
        if isPossibleGame(games):
            if debug:
                print(game_id, games)
            output += int(game_id)
    return output

def part2(lines, debug=False):
    # Max de chaque couleur, valeur multipliée entre elle et ajouté à output
    output = 0
    for line in lines:
        _, games = line.split(":")
        games = games.split("; ")
        valMaxColor = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for game in games:
            colors = game.split(", ")
            for color in colors:
                val, col = color.split()
                valMaxColor[col] = max(int(val), valMaxColor[col])
        if debug:
            print(valMaxColor, valMaxColor["red"]*valMaxColor["blue"]*valMaxColor["green"])
        output += valMaxColor["red"]*valMaxColor["blue"]*valMaxColor["green"]
    return output

if __name__ == "__main__":
    exLines = getlinesExample(testEx)
    print(part1(exLines, True))
    inputLines = getlinesInput()
    print(part1(inputLines))
    exLines2 = getlinesExample(testEx)
    print(part2(exLines2, True))
    print(part2(inputLines))