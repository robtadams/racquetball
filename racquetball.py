import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
    response = input("Play again? ")
    if response:
        main()
    else:
        return

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates n games of racquetball between players whose
    #   abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B
    serving = True
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving:
            if random.randint(0, 100) < probA:
                scoreA = scoreA + 1
            else:
                serving = False
        else:
            if random.randint(0, 100) < probB:
                scoreB = scoreB + 1
            else:
                serving = True
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for racquetball game
    # Returns True if the game is over, False otherwise
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == "__main__":
    main()



    
            
