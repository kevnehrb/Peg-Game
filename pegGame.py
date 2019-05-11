import tkinter
from tkinter import *
from tkinter import TOP, BOTTOM

root = Tk()

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

        #self.play()
        
    window = Canvas(root, width = 300, height = 300)
    window.pack()
    window.create_rectangle(5, 5, 300, 300, fill="black")
    window.create_polygon(5, 300, 150, 5, 300, 300, fill="yellow")

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

    #window.itemconfig(slot0, fill="blue") # change color

    def createOptionButtons(self):
        self.restartButton = Button(optionFrame, text = "Restart", fg = "blue", command = self.reset())
        self.restartButton.pack(side="left")

        self.statsButton = Button(optionFrame, text = "Statistics", fg = "purple")
        self.statsButton.pack(side="left")

        self.quitButton = Button(optionFrame, text = "Quit", fg = "red", command = self.master.destroy)
        self.quitButton.pack(side="left")
        

    def reset(self):
        self.solved = False
        self.activePegs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.removedPegs = [0]
        self.totMoves = 0

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

    def outOfMoves(self):
        #goes through active pegs and checks for all possible moves, if there are more return false, if theres 1 peg left, user wins else loses
        possibleMoves = []

        if len(self.activePegs) == 1:
            #user has won
            self.solved = True
            return True

        for each in self.activePegs:
            possibleMoves = possibleMoves + self.availableMoves(each)
 
        if not possibleMoves:
            #there are no possible moves left
            return True
        else:
            return False
         
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

    def onclick(event):
        peg = b.window.find_closest(event.x, event.y)
        current_color = b.window.itemcget(peg, 'fill')

        pegList = b.window.gettags(peg)
        pegID = pegList[0]
        pegID = int(pegID)
        print(pegID)

        isPeg = b.window.type(peg)
        if isPeg == "oval":
            if b.sourceSelected == -1:
                if current_color == 'red':
                    b.window.itemconfig(peg, fill='blue')
                    b.sourceSelected = pegID
            else:
                if current_color == 'blue':
                    b.window.itemconfig(peg, fill='red') 
                    b.sourceSelected = -1
                elif current_color == 'white':
                    pass
                    #check if 2nd click and sourceSelected is a valid move, then do some funky shit roflmfao

    def makeMove(event):
        peg = b.window.find_closest(event.x, event.y)
        #get the number id of the selected peg
        #build a list of available moves using selected peg as source spot
        #if the pegs color is white (signifying emptiness) or if the list of available moves is empty, invalid click don't register
        
        #else select peg and set source equal to tag number, this is the source spot
       # b.window.itemconfig(peg, fill='blue')
        #while following clicks are not valid jump, based on list of available moves [2]position
            #ignore click
        #make jump
            #builtJump = b.buildJumpVariable(source, destination)
            #b.makeJump(jump variable in for mat of [x,y,z])
            #change color of source and jumped pegs to white to signify open space, change color of destination to red to signify occupied space



    b.window.bind('<ButtonPress-1>', onclick)
    b.window.pack()
    root.mainloop()
