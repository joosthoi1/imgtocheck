from tkinter import *
class grid:
    def __init__(self, root, numberx, numbery, text=''):
        self.root = root
        self.boxlist, self.varlist = [], []
        self.numberx, self.numbery = numberx, numbery
        self.xgrid, self.ygrid = 0, 0
        self.root.title('gridcreation')
        self.text = text    #setting up some standard variables
        self.coordrost = [[i for i in range(self.numberx*x,self.numberx+self.numberx*x)] for x in range(numbery)] #creates a list that looks a little like this:
        """
        [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
        """

        for i in range(10000):  #puts checkboxes in the window on the right posisition
            self.varlist.append(IntVar())
            self.boxlist.append(Checkbutton(self.root, text=self.text, variable=self.varlist[i]))
            self.boxlist[i].grid(row=self.ygrid, sticky=W, column=self.xgrid)
            self.boxlist[i].configure(bg='light gray')
            self.xgrid += 1
            if self.xgrid == self.numberx:
                self.ygrid += 1
                self.xgrid = 0

            if self.ygrid == self.numbery:
                break


    def coords(self, x, y):
        return self.coordrost[self.numbery-y][x-1] #with help of the defined cordrost is able to convert (3, 5) into something like 124 (example, might not apply)
    def uncoords(self, coord):
        for i in range(len(self.coordrost)): #with help of coordrost is able to convert something like 124 into [3, 5] (example, might not apply)
            if coord in self.coordrost[i]:
                x1 = self.coordrost[i].index(coord) + 1
                y1 = self.numbery - i
                return [x1, y1]
