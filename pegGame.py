import tkinter
import time
from tkinter import *
from tkinter import BOTTOM
from tkinter import messagebox



root = Tk()

#frame for the buttons
optionFrame = Frame(root)
optionFrame.pack(side = BOTTOM)

class Main():
    def __init__(self, master):
        self.master = master
        self.createOptionButtons()
        #each jump is represented by 3 numbers, (starting space, the jumped over space, and destination)
        self.jumps = [[0,1,3], [0,2,5], [1,3,6], [1,4,8], [2,4,7], [2,5,9], 
                      [3,1,0], [3,4,5], [3,6,10], [3,7,12], [4,7,11], [4,8,13],
                      [5,2,0], [5,4,3], [5,8,12], [5,9,14], [6,3,1], [6,7,8],
                      [7,4,2], [7,8,9], [8,4,1], [8,7,6], [9,5,2], [9,8,7],
                      [10,6,3], [10,11,12], [11,7,4], [11,12,13], [12,7,3], [12,8,5],
                      [12,11,10], [12,13,14], [13,8,4], [13,12,11], [14,9,5], [14,13,12]]

        self.solved = False
        self.activePegs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.removedPegs = [0]
        self.totMoves = 0
        self.sourceSelected = -1
        
    window = Canvas(root, width = 300, height = 300)
    window.pack()
    window.create_rectangle(5, 5, 300, 300, fill="black", tags=("background",))
    window.create_polygon(5, 300, 150, 5, 300, 300, fill="yellow", tags=("board",))

    #create the board buttons
    slot0 = window.create_oval(125, 50, 165, 90, fill="white", tags=(0,))
    slot1 = window.create_oval(100, 100, 140, 140, fill="red", tags=(1,))
    slot2 = window.create_oval(150, 100, 190, 140, fill="red", tags=(2,))
    slot3 = window.create_oval(75, 150, 115, 190, fill="red", tags=(3,))
    slot4 = window.create_oval(125, 150, 165, 190, fill="red", tags=(4,))
    slot5 = window.create_oval(175, 150, 215, 190, fill="red", tags=(5,))
    slot6 = window.create_oval(50, 200, 90, 240, fill="red", tags=(6,))
    slot7 = window.create_oval(100, 200, 140, 240, fill="red", tags=(7,))
    slot8 = window.create_oval(150, 200, 190, 240, fill="red", tags=(8,))
    slot9 = window.create_oval(200, 200, 240, 240, fill="red", tags=(9,))
    slot10 = window.create_oval(25, 250, 65, 290, fill="red", tags=(10,))
    slot11 = window.create_oval(75, 250, 115, 290, fill="red", tags=(11,))
    slot12 = window.create_oval(125, 250, 165, 290, fill="red", tags=(12,))
    slot13 = window.create_oval(175, 250, 215, 290, fill="red", tags=(13,))
    slot14 = window.create_oval(225, 250, 265, 290, fill="red", tags=(14,))

    # creates the bottom row of buttons in the optionsFrame
    def createOptionButtons(self):
        self.restartButton = Button(optionFrame, text = "Restart", fg = "blue", command = self.reset)
        self.restartButton.pack(side="left")

        self.statsButton = Button(optionFrame, text = "Statistics", fg = "purple", command = self.getStats)
        self.statsButton.pack(side="left")

        self.quitButton = Button(optionFrame, text = "Quit", fg = "red", command = self.master.destroy)
        self.quitButton.pack(side="left")
    
    # adds the amount of moves in a current game to the total moves stat
    def statUpdateMoves(self):
        file = open("config.txt", "r")
        wordLine = file.readline()
        wordList = wordLine.split()
        file.close()
        currMoves = int(wordList[1])
        currMoves += self.totMoves
        wordList[1] = str(currMoves)
        newLine = " ".join(wordList)
        file = open("config.txt", "w")
        file.write(newLine)
        file.close()

    # will add 1 to games attempted every time a user plays a game
    def statUpdateGamesAttempted(self):
        file = open("config.txt", "r")
        wordLine = file.readline()
        wordList = wordLine.split()
        file.close()
        currAttempts = int(wordList[5])
        currAttempts += 1
        wordList[5] = str(currAttempts)
        newLine = " ".join(wordList)
        file = open("config.txt", "w")
        file.write(newLine)
        file.close()

    # will add 1 to games won when a user wins the game
    def statUpdateGamesWon(self):
        file = open("config.txt", "r")
        wordLine = file.readline()
        wordList = wordLine.split()
        file.close()
        currGames = int(wordList[3])
        currGames += 1
        wordList[3] = str(currGames)
        newLine = " ".join(wordList)
        file = open("config.txt", "w")
        file.write(newLine)
        file.close()

    # checks to see if a game won is a new record finish
    def statUpdateTime(self, newTime):
        file = open("config.txt", "r")
        wordLine = file.readline()
        wordList = wordLine.split()
        file.close()
        
        if(wordList[7] == 'none'):
            wordList[7] = str(newTime)

        currSeconds = float(wordList[7])
        if(newTime < currSeconds):
            wordList[7] = str(newTime)
        else:
            wordList[7] = str(currSeconds)
        newLine = " ".join(wordList)
        file = open("config.txt", "w")
        file.write(newLine)
        file.close()

    #obtain current stats to be given in a message box to the user when they ask for it
    def getStats(self):
        file = open("config.txt", "r")
        wordLine = file.readline()
        wordList = wordLine.split()
        file.close()
        newLine = wordList[0] + " " + wordList[1] + "\n" + wordList[2] + " " + wordList[3] + "\n" + wordList[4] + " " + wordList[5] + "\n" + wordList[6] + " " + wordList[7] + " seconds"
        messagebox.showinfo("Statistics", newLine)

    # resets the board back to the beginning
    def reset(self):

        self.statUpdateMoves()
        self.statUpdateGamesAttempted()

        self.solved = False
        self.activePegs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.removedPegs = [0]
        self.totMoves = 0
        self.sourceSelected = -1
        
        self.window.itemconfig(self.slot0, fill='white')
        self.window.itemconfig(self.slot1, fill='red')
        self.window.itemconfig(self.slot2, fill='red')
        self.window.itemconfig(self.slot3, fill='red')
        self.window.itemconfig(self.slot4, fill='red')
        self.window.itemconfig(self.slot5, fill='red')
        self.window.itemconfig(self.slot6, fill='red')
        self.window.itemconfig(self.slot7, fill='red')
        self.window.itemconfig(self.slot8, fill='red')
        self.window.itemconfig(self.slot9, fill='red')
        self.window.itemconfig(self.slot10, fill='red')
        self.window.itemconfig(self.slot11, fill='red')
        self.window.itemconfig(self.slot12, fill='red')
        self.window.itemconfig(self.slot13, fill='red')
        self.window.itemconfig(self.slot14, fill='red')

        startTime = time.time()

    # used in avaliable moves to check if there is a peg in a particular slot
    def spaceOpen(self,space):
        for each in self.activePegs:
            if each == space:
                #there is a peg in the desired spot already
                return False
        return True

    def availableMoves(self,selectedPeg):
        #returns a list of all possible jumps the selected peg can make
        possibleMoves = []

        for each in self.jumps:
            if each[0] == selectedPeg:
                if self.spaceOpen(each[2]) == True and self.spaceOpen(each[1]) == False:
                    possibleMoves.append(each)
  
        return possibleMoves

    def makeJump(self, selectedJump):
        #jumps the peg, removes the jumped space from the active list and places it in the removed list
        self.activePegs.remove(selectedJump[0])
        self.activePegs.remove(selectedJump[1])
        self.activePegs.append(selectedJump[2])
        self.removedPegs.append(selectedJump[0])
        self.removedPegs.append(selectedJump[1])
        self.removedPegs.remove(selectedJump[2])
        self.totMoves += 1
         
    def buildJumpVariable(self,source,destination):
        #makes a list of the source, jump, and destination
        jumpList = []
        jumpList.append(source)
        for each in self.jumps:
            if each[0] == source and each[2] == destination:
                jumpedPeg = each[1]
        jumpList.append(jumpedPeg)
        jumpList.append(destination)
        return jumpList



if __name__ == "__main__":
    b = Main(root)
    b.startTime = time.time()
    
    def onclick(event):

        peg = b.window.find_closest(event.x, event.y)
        current_color = b.window.itemcget(peg, 'fill')

        isPeg = b.window.type(peg)
        if isPeg == "oval":

            pegList = b.window.gettags(peg)
            pegID = pegList[0]
            pegID = int(pegID)

            if b.sourceSelected == -1:
                if current_color == 'red':
                    b.window.itemconfig(peg, fill='blue')
                    b.sourceSelected = pegID
            else:
                if current_color == 'blue':
                    b.window.itemconfig(peg, fill='red') 
                    b.sourceSelected = -1
                elif current_color == 'white':
                    #check to make sure if 2nd click and sourceSelected is a valid move
                    potentialMoves = b.availableMoves(b.sourceSelected)
                    if potentialMoves:
                        for each in potentialMoves:
                            if each[2] == pegID:
                                theJump = b.buildJumpVariable(b.sourceSelected, pegID)
                        b.makeJump(theJump)

                        if(theJump[0] == 0):
                            b.window.itemconfig(b.slot0, fill='white')
                        elif(theJump[0] == 1):
                            b.window.itemconfig(b.slot1, fill='white')
                        elif(theJump[0] == 2):
                            b.window.itemconfig(b.slot2, fill='white')
                        elif(theJump[0] == 3):
                            b.window.itemconfig(b.slot3, fill='white')
                        elif(theJump[0] == 4):
                            b.window.itemconfig(b.slot4, fill='white')
                        elif(theJump[0] == 5):
                            b.window.itemconfig(b.slot5, fill='white')
                        elif(theJump[0] == 6):
                            b.window.itemconfig(b.slot6, fill='white')
                        elif(theJump[0] == 7):
                            b.window.itemconfig(b.slot7, fill='white')
                        elif(theJump[0] == 8):
                            b.window.itemconfig(b.slot8, fill='white')
                        elif(theJump[0] == 9):
                            b.window.itemconfig(b.slot9, fill='white')
                        elif(theJump[0] == 10):
                            b.window.itemconfig(b.slot10, fill='white')
                        elif(theJump[0] == 11):
                            b.window.itemconfig(b.slot11, fill='white')
                        elif(theJump[0] == 12):
                            b.window.itemconfig(b.slot12, fill='white')
                        elif(theJump[0] == 13):
                            b.window.itemconfig(b.slot13, fill='white')
                        elif(theJump[0] == 14):
                            b.window.itemconfig(b.slot14, fill='white')

                        if(theJump[1] == 0):
                            b.window.itemconfig(b.slot0, fill='white')
                        elif(theJump[1] == 1):
                            b.window.itemconfig(b.slot1, fill='white')
                        elif(theJump[1] == 2):
                            b.window.itemconfig(b.slot2, fill='white')
                        elif(theJump[1] == 3):
                            b.window.itemconfig(b.slot3, fill='white')
                        elif(theJump[1] == 4):
                            b.window.itemconfig(b.slot4, fill='white')
                        elif(theJump[1] == 5):
                            b.window.itemconfig(b.slot5, fill='white')
                        elif(theJump[1] == 6):
                            b.window.itemconfig(b.slot6, fill='white')
                        elif(theJump[1] == 7):
                            b.window.itemconfig(b.slot7, fill='white')
                        elif(theJump[1] == 8):
                            b.window.itemconfig(b.slot8, fill='white')
                        elif(theJump[1] == 9):
                            b.window.itemconfig(b.slot9, fill='white')
                        elif(theJump[1] == 10):
                            b.window.itemconfig(b.slot10, fill='white')
                        elif(theJump[1] == 11):
                            b.window.itemconfig(b.slot11, fill='white')
                        elif(theJump[1] == 12):
                            b.window.itemconfig(b.slot12, fill='white')
                        elif(theJump[1] == 13):
                            b.window.itemconfig(b.slot13, fill='white')
                        elif(theJump[1] == 14):
                            b.window.itemconfig(b.slot14, fill='white')

                        b.window.itemconfig(peg, fill='red')
                        b.sourceSelected = -1

                        if len(b.activePegs) == 1:
                            #user has won
                            b.solved = True
                            b.statUpdateGamesWon()
                            endTime = time.time()
                            newTime = endTime - b.startTime
                            b.statUpdateTime(newTime)
                            messagebox.showinfo("Winner!", "You won!")
                        else:
                            possibleMoves = []
                            for each in b.activePegs:
                                possibleMoves = possibleMoves + b.availableMoves(each)
                            if not possibleMoves:
                                #there are no more moves left. return
                                messagebox.showinfo("Try Again", "You lost, hit restart to try again!")
                        

    b.window.bind('<ButtonPress-1>', onclick)
    b.window.pack()
    root.mainloop()
    
