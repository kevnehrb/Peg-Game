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

        #self.play()
        
    window = Canvas(root, width = 300, height = 300)
    window.pack()
    window.create_rectangle(5, 5, 300, 300, fill="black")
    window.create_polygon(5, 300, 150, 5, 300, 300, fill="yellow")

    #create the board buttons
    slot0 = window.create_oval(125, 50, 165, 90, fill="white", tags=("0",))
    slot1 = window.create_oval(100, 100, 140, 140, fill="red")
    slot2 = window.create_oval(150, 100, 190, 140, fill="red")
    slot3 = window.create_oval(75, 150, 115, 190, fill="red")
    slot4 = window.create_oval(125, 150, 165, 190, fill="red")
    slot5 = window.create_oval(175, 150, 215, 190, fill="red")
    slot6 = window.create_oval(50, 200, 90, 240, fill="red")
    slot7 = window.create_oval(100, 200, 140, 240, fill="red")
    slot8 = window.create_oval(150, 200, 190, 240, fill="red")
    slot9 = window.create_oval(200, 200, 240, 240, fill="red")
    slot10 = window.create_oval(25, 250, 65, 290, fill="red")
    slot11 = window.create_oval(75, 250, 115, 290, fill="red")
    slot12 = window.create_oval(125, 250, 165, 290, fill="red")
    slot13 = window.create_oval(175, 250, 215, 290, fill="red")
    slot14 = window.create_oval(225, 250, 265, 290, fill="red")

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

    def onclick(event):
        peg = window.find_closest(event.x, event.y)

        current_color = window.itemcget(peg, 'fill')

        isPeg = window.type(peg)
        if isPeg == "oval":
            if current_color == 'red':
                window.itemconfig(peg, fill='blue')
            else:
                window.itemconfig(peg, fill='red') 
         
         
   
if __name__ == "__main__":
    Main(root)
    root.mainloop()












b = Board()
#print(b.activePegs)
#print(b.removedPegs)
#b.makeJump((3,1,0))
#print(b.activePegs)
#print(b.removedPegs)
#print(b.availableMoves(5))
#print(b.totMoves)
boole = b.outOfMoves()
if boole == True:
    print("true")
else:
    print("false")
print("end")
