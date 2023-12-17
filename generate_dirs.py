import os

CURR_PATH = os.getcwd()

for i in range(2, 25):
    path = os.path.join(CURR_PATH, f"Day{i}")
    inputPath = os.path.join(path, "input.txt")
    codePath = os.path.join(path, f"day{i}.py")
    if not os.path.isdir(path):
        os.makedirs(path)
        inputFile = open(inputPath, "w")
        codeFile = open(codePath, "w")