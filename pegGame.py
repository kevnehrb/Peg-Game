#import tkinter as tk
#root = tk.Tk()
#root.mainloop()

print("yahoo")
class Board:

    def __init__(self):
        #each jump is represented by 3 numbers, (starting space, the jumped over space, and destination)
        self.jumps = [[0,1,3],
                      [0,2,5],
                      [1,3,6],
                      [1,4,8],
                      [2,4,7],
                      [2,5,9],
                      [3,1,0],
                      [3,4,5],
                      [3,6,10],
                      [3,7,12],
                      [4,7,11],
                      [4,8,13],
                      [5,4,3],
                      [5,8,12],
                      [5,9,14],
                      [6,3,1],
                      [6,7,8],
                      [7,4,2],
                      [7,8,9],
                      [8,4,1],
                      [8,7,6],
                      [9,5,2],
                      [9,8,7],
                      [10,6,3],
                      [10,11,12],
                      [11,7,4],
                      [11,12,13],
                      [12,7,3],
                      [12,8,5],
                      [12,11,10],
                      [12,13,14],
                      [13,8,4],
                      [13,12,11],
                      [14,9,5],
                      [14,13,12]]
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











b = Board()
print(b.activePegs)
print(b.removedPegs)
b.makeJump((3,1,0))
print(b.activePegs)
print(b.removedPegs)
print(b.availableMoves(5))
print("end")
