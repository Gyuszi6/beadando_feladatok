import random
import sys

def writeToFile(championship):
    f = open("output.txt", "w")
    k = 4
    sokadik = False
    for i in range(len(championship)):
        for j in range(len(championship[i])):
            if i == 0 or i == 1:
                f.write("\t" * (i + 1) + championship[i][j] + "\t" * (i + 1))

            else:
                f.write("\t" * (k) + championship[i][j] + "\t" * (k))
                sokadik = True

        f.write("\n")

        for j in range(len(championship[i])):
            if len(championship[i]) == 1:
                continue
            if i == 0 or i == 1:
                f.write("\t" * (i + 1) + "  |  " + "\t" * (i + 1))
            else:
                f.write("\t" * (k) + "  |  " + "\t" * (k))

        f.write("\n")
        leftSide = True
        for j in range(len(championship[i])):
            if leftSide:
                if len(championship[i]) == 1:
                    continue
                if i == 0 or i == 1:
                    f.write("\t" * (i + 1) + "  " + "--------" * (i + 1))
                else:
                    f.write("\t" * (k) + "  " + "--------" * (k))
                leftSide = False
            else:
                if len(championship[i]) == 1:
                    continue
                if i == 0 or i == 1:
                    f.write("--------" * (i + 1) + "  " + "\t" * (i + 1))
                else:
                    f.write("--------" * (k) + "\t" * (k) + "  ")
                leftSide = True
        f.write("\n")
        if sokadik:
            k = k * 2

def fordulo(actualTeams):
    winners = []
    i = 0
    lucky = ""
    if (len(actualTeams) % 2 == 1):
        lucky = actualTeams[len(actualTeams) - 1]
    while i < (len(actualTeams) - 1):
        x = random.randint(0, 1)
        if x == 0:
            winner = actualTeams[i]
            winners.append(winner)
        else:
            winner = actualTeams[i + 1]
            winners.append(winner)
        i = i + 2
    if lucky != "":
        winners.append(lucky)
    return winners


def championshipSimulation(numberOfTeams):
    championship = []
    teams = []
    for i in range(1, numberOfTeams +1):
        team = "team" + str(i)
        teams.append(team)
    championship.append(teams)
    i = 1
    championship.append(fordulo(championship[i - 1]))
    while len(championship[i]) != 1:
        i = i + 1
        championship.append(fordulo(championship[i - 1]))
    writeToFile(championship)

championshipSimulation(int(sys.argv[1]))


